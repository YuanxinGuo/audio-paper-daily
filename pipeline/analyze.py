"""Analyze unprocessed papers using DeepSeek and persist results."""
from __future__ import annotations
import json
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from openai import OpenAI
from tenacity import retry, stop_after_attempt, wait_exponential

from config import (DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL, DEEPSEEK_MODEL,
                    LLM_CONCURRENCY, LLM_TIMEOUT, TAG_ALIASES)
from db import connect, get_unanalyzed, save_analysis

PROMPT_TEMPLATE = (Path(__file__).parent / "prompts" / "analyze.txt").read_text(
    encoding="utf-8"
)

if not DEEPSEEK_API_KEY:
    print("[analyze] WARN: DEEPSEEK_API_KEY not set; skipping analysis.")
    sys.exit(0)

client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url=DEEPSEEK_BASE_URL)


def _canonicalize_tag(tag: str) -> str:
    if not tag:
        return tag
    if not tag.startswith("#"):
        tag = "#" + tag
    return TAG_ALIASES.get(tag, tag)


@retry(stop=stop_after_attempt(3), wait=wait_exponential(min=2, max=20))
def _call_llm(title: str, abstract: str) -> dict:
    prompt = PROMPT_TEMPLATE.replace("{title}", title).replace(
        "{abstract}", abstract[:6000]
    )
    resp = client.chat.completions.create(
        model=DEEPSEEK_MODEL,
        messages=[
            {"role": "system",
             "content": "You return ONLY a single valid JSON object."},
            {"role": "user", "content": prompt},
        ],
        response_format={"type": "json_object"},
        temperature=0.2,
        timeout=LLM_TIMEOUT,
    )
    content = resp.choices[0].message.content
    data = json.loads(content)

    # normalise
    data["score"] = float(data.get("score", 0.0))
    data["tier"] = (data.get("tier") or "中等").strip()
    data["main_task"] = _canonicalize_tag(data.get("main_task", "#其他"))
    data["tags"] = [_canonicalize_tag(t) for t in data.get("tags", []) if t]
    return data


def _analyze_one(row) -> tuple[str, dict | None, str | None]:
    try:
        result = _call_llm(row["title"], row["abstract"])
        return row["arxiv_id"], result, None
    except Exception as e:
        return row["arxiv_id"], None, str(e)


def main() -> None:
    with connect() as conn:
        pending = get_unanalyzed(conn)
    print(f"[analyze] pending={len(pending)}")
    if not pending:
        return

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
            print(f"  ✓ {arxiv_id}: {result.get('score')} {result.get('main_task')}")

    print(f"[analyze] ok={ok} fail={fail}")


if __name__ == "__main__":
    main()
