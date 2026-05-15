"""Analyze unprocessed papers using DeepSeek and persist results."""
from __future__ import annotations
import json
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from openai import OpenAI
from tenacity import retry, stop_after_attempt, wait_exponential

from config import (DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL, DEEPSEEK_MODEL,
                    LLM_CONCURRENCY, LLM_TIMEOUT, TAG_ALIASES,
                    FOCUS_TAGS, SCORE_FOCUS_BONUS,
                    DAILY_ANALYSIS_LIMIT, FOCUS_KEYWORDS)
from db import connect, get_unanalyzed, save_analysis

PROMPT_TEMPLATE = (Path(__file__).parent / "prompts" / "analyze.txt").read_text(
    encoding="utf-8"
)

# Lazily build the OpenAI client so import works even when no key is set
# (e.g. local syntax checks or running render-only).
client = (
    OpenAI(api_key=DEEPSEEK_API_KEY, base_url=DEEPSEEK_BASE_URL)
    if DEEPSEEK_API_KEY else None
)


def _canonicalize_tag(tag: str) -> str:
    if not tag:
        return tag
    tag = tag.strip()
    if not tag.startswith("#"):
        tag = "#" + tag
    # Try direct alias first, then case-insensitive
    if tag in TAG_ALIASES:
        return TAG_ALIASES[tag]
    low = tag.lower()
    for k, v in TAG_ALIASES.items():
        if k.lower() == low:
            return v
    return tag


def _focus_bonus(main_task: str, tags: list[str]) -> float:
    pool = {main_task} | set(tags)
    return SCORE_FOCUS_BONUS if pool & FOCUS_TAGS else 0.0


def _validate_and_normalise(data: dict) -> dict:
    """Coerce / fill defaults; preserve raw_score before focus bonus."""
    raw_score = float(data.get("score", 0.0) or 0.0)
    raw_score = max(0.0, min(10.0, raw_score))

    main_task = _canonicalize_tag(data.get("main_task") or "#其他")
    tags = [_canonicalize_tag(t) for t in (data.get("tags") or []) if t]
    tags = list(dict.fromkeys(tags))[:4]  # dedupe + cap

    bonus = _focus_bonus(main_task, tags)
    final_score = min(10.0, raw_score + bonus)

    # Re-derive tier if absent or mismatching
    tier = (data.get("tier") or "").strip()
    if not tier:
        if final_score >= 8.0:
            tier = "前10%"
        elif final_score >= 7.0:
            tier = "前25%"
        elif final_score >= 6.0:
            tier = "前50%"
        elif final_score >= 5.0:
            tier = "中等"
        else:
            tier = "后50%"

    rec = (data.get("recommendation") or "optional").lower()
    if rec not in {"must_read", "optional", "skip"}:
        rec = "optional"

    def _list(key, n=8):
        v = data.get(key)
        if not isinstance(v, list):
            return []
        return [str(x).strip() for x in v if x][:n]

    res = data.get("resources") or {}
    if not isinstance(res, dict):
        res = {}
    resources = {
        "code_url": (res.get("code_url") or "").strip(),
        "project_url": (res.get("project_url") or "").strip(),
        "hf_url": (res.get("hf_url") or "").strip(),
        "demo_url": (res.get("demo_url") or "").strip(),
        "dataset_urls": [u for u in (res.get("dataset_urls") or [])
                         if isinstance(u, str) and u.strip()][:4],
    }
    # discard obviously fake URLs
    for k in ("code_url", "project_url", "hf_url", "demo_url"):
        if resources[k] and not resources[k].startswith(("http://", "https://")):
            resources[k] = ""

    # Validate results_table: list of dicts with required keys.
    rt_in = data.get("results_table")
    results_table: list[dict] = []
    if isinstance(rt_in, list):
        for r in rt_in[:6]:
            if not isinstance(r, dict):
                continue
            results_table.append({
                "metric":   str(r.get("metric") or "").strip(),
                "dataset":  str(r.get("dataset") or "").strip(),
                "baseline": str(r.get("baseline") or "").strip(),
                "ours":     str(r.get("ours") or "").strip(),
                "delta":    str(r.get("delta") or "").strip(),
            })

    return {
        "score": final_score,
        "raw_score": raw_score,
        "tier": tier,
        "main_task": main_task,
        "tags": tags,
        "tldr": data.get("tldr") or "",
        "reading_suggestion": data.get("reading_suggestion") or "",
        "limitations": data.get("limitations") or "",
        "recommendation": rec,
        "first_authors": _list("first_authors", 4),
        "corresponding_authors": _list("corresponding_authors", 4),
        "affiliations": _list("affiliations", 4),
        "resources": resources,
        # New v3 fields:
        "background": data.get("background") or "",
        "innovations": _list("innovations", 5),
        "architecture": data.get("architecture") or "",
        "datasets": _list("datasets", 4),
        "results_table": results_table,
        "results_text": data.get("results_text") or "",
        "conclusion": data.get("conclusion") or "",
    }


@retry(stop=stop_after_attempt(3), wait=wait_exponential(min=2, max=20))
def _call_llm(title: str, abstract: str, authors: str) -> dict:
    prompt = (PROMPT_TEMPLATE
              .replace("{title}", title)
              .replace("{authors}", authors or "（作者列表未给出）")
              .replace("{abstract}", abstract[:6000]))
    resp = client.chat.completions.create(
        model=DEEPSEEK_MODEL,
        messages=[
            {"role": "system",
             "content": "你必须只返回一个合法的 JSON 对象，不要任何额外文本。"},
            {"role": "user", "content": prompt},
        ],
        response_format={"type": "json_object"},
        temperature=0.2,
        timeout=LLM_TIMEOUT,
    )
    content = resp.choices[0].message.content
    raw = json.loads(content)
    return _validate_and_normalise(raw)


def _analyze_one(row) -> tuple[str, dict | None, str | None]:
    try:
        result = _call_llm(row["title"], row["abstract"], row["authors"] or "")
        return row["arxiv_id"], result, None
    except Exception as e:
        return row["arxiv_id"], None, str(e)


def _is_focus_candidate(row) -> bool:
    """Cheap keyword pre-filter: does the paper look like a focus-area
    paper based on its title + abstract?"""
    haystack = f"{row['title']} {row['abstract']}".lower()
    for kws in FOCUS_KEYWORDS.values():
        for kw in kws:
            if kw in haystack:
                return True
    return False


def _select_today(pending: list, limit: int) -> list:
    """Pick at most `limit` papers from pending, focus candidates first."""
    focus = [p for p in pending if _is_focus_candidate(p)]
    other = [p for p in pending if not _is_focus_candidate(p)]
    chosen = focus[:limit]
    if len(chosen) < limit:
        chosen += other[: limit - len(chosen)]
    return chosen


def main() -> None:
    with connect() as conn:
        pending = get_unanalyzed(conn)
    print(f"[analyze] pending={len(pending)}")
    if not pending:
        print("[analyze] nothing to do")
        return

    selected = _select_today(pending, DAILY_ANALYSIS_LIMIT)
    selected_ids = {p["arxiv_id"] for p in selected}
    n_focus = sum(1 for p in selected if _is_focus_candidate(p))
    skipped_ids = [p["arxiv_id"] for p in pending if p["arxiv_id"] not in selected_ids]

    # Discard the skipped ones from the DB so they don't accumulate forever.
    if skipped_ids:
        with connect() as conn:
            conn.executemany(
                "DELETE FROM papers WHERE arxiv_id = ?",
                [(aid,) for aid in skipped_ids],
            )

    print(f"[analyze] picked {len(selected)} (focus={n_focus}, "
          f"other={len(selected) - n_focus}); discarded {len(skipped_ids)}")
    pending = selected

    ok = fail = 0
    with ThreadPoolExecutor(max_workers=LLM_CONCURRENCY) as pool:
        futures = [pool.submit(_analyze_one, p) for p in pending]
        for fut in as_completed(futures):
            arxiv_id, result, err = fut.result()
            if err:
                fail += 1
                print(f"  ! {arxiv_id}: {err}")
                continue
            with connect() as conn:
                save_analysis(conn, arxiv_id, result)
            ok += 1
            bonus = " [+focus]" if result["score"] != result["raw_score"] else ""
            print(f"  ok {arxiv_id}: {result['score']:.1f} "
                  f"{result['main_task']}{bonus}")

    print(f"[analyze] ok={ok} fail={fail}")


if __name__ == "__main__":
    main()
