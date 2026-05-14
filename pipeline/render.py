"""Render today's analyzed papers into Hugo content.

Layout:
  site/content/posts/<date>/index.md           ← daily digest (list)
  site/content/posts/<date>/<slug>.md          ← per-paper detail page
"""
from __future__ import annotations
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

from config import POSTS_DIR, FOCUS_TAGS
from db import connect, papers_for_date

MEDALS = ["🥇", "🥈", "🥉"]


# --------------------------------------------------------------------------- helpers


def _slugify(text: str, max_len: int = 60) -> str:
    s = (text or "").lower()
    s = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", s)
    s = s.strip("-")
    return s[:max_len] or "paper"


def _rank_marker(i: int) -> str:
    if i < 3:
        return MEDALS[i]
    return f"{i + 1}."


def _bar(n: int, total_max: int, width: int = 10) -> str:
    if total_max <= 0:
        return ""
    filled = max(1, round(width * n / total_max))
    return "█" * filled


def _percentile_bucket(score: float) -> str:
    if score >= 8.0:
        return "前10%"
    if score >= 7.0:
        return "前25%"
    if score >= 6.0:
        return "前50%"
    if score >= 5.0:
        return "中等"
    return "后50%"


def _is_focus(row) -> bool:
    pool = {row["main_task"] or ""}
    try:
        pool.update(json.loads(row["tags"] or "[]"))
    except Exception:
        pass
    return bool(pool & FOCUS_TAGS)


def _safe_json(s: str | None, default):
    try:
        return json.loads(s or "")
    except Exception:
        return default


# --------------------------------------------------------------------------- per-paper page


def _render_paper_page(row, daily_dir: Path, daily_url: str) -> str:
    """Write a per-paper markdown file. Returns its slug for the index."""
    slug = _slugify(row["title"]) + "-" + row["arxiv_id"].replace(".", "-")
    page_path = daily_dir / f"{slug}.md"

    mc = _safe_json(row["model_card"], {})
    innovations = mc.get("innovations") or []
    datasets = mc.get("datasets") or []
    tags = _safe_json(row["tags"], [])
    main_task = row["main_task"] or ""

    front_tags_for_yaml = sorted({main_task, *tags} - {""})

    rec_label = {
        "must_read": "🔥 强烈推荐通读",
        "optional":  "⏳ 按需阅读",
        "skip":      "✋ 可以跳过",
    }.get((row["recommendation"] or "optional"), "⏳ 按需阅读")

    focus_badge = ""
    if _is_focus(row):
        focus_badge = "🎯 **本站重点关注领域** · 评分已 +1\n\n"

    out: list[str] = []
    out.append("---")
    out.append(f'title: {json.dumps(row["title"], ensure_ascii=False)}')
    out.append(f'date: {row["fetch_date"][:10]}T09:00:00+08:00')
    out.append("draft: false")
    out.append('categories: ["论文详情"]')
    out.append("tags: " + json.dumps(front_tags_for_yaml, ensure_ascii=False))
    out.append('summary: ' + json.dumps(row["tldr"] or row["title"][:60],
                                         ensure_ascii=False))
    out.append("ShowToc: true")
    out.append("---")
    out.append("")

    # Top metadata strip
    out.append(f"**评分**: {row['score']:.1f} / 10  ·  "
               f"**分档**: {row['tier'] or _percentile_bucket(row['score'])}  ·  "
               f"**主任务**: {main_task}  ·  **建议**: {rec_label}")
    out.append("")
    if focus_badge:
        out.append(focus_badge)
    if tags:
        out.append("**标签**: " + " · ".join(tags))
        out.append("")
    out.append(f"[← 返回 {row['fetch_date'][:10]} 速递]({daily_url})  ·  "
               f"[arxiv]({row['html_url']})  ·  [pdf]({row['pdf_url']})")
    out.append("")
    out.append("---")
    out.append("")

    # TL;DR
    if row["tldr"]:
        out.append("## 📌 一句话总结")
        out.append("")
        out.append(f"> {row['tldr']}")
        out.append("")

    # Reading suggestion
    if row["reading_suggestion"]:
        out.append("## 📖 阅读建议")
        out.append("")
        out.append(row["reading_suggestion"])
        out.append("")

    # Model card
    out.append("## 🧩 模型一栏概览")
    out.append("")
    out.append("| 项 | 内容 |")
    out.append("| --- | --- |")
    if mc.get("scenario"):
        out.append(f"| 应用场景 | {mc['scenario']} |")
    if innovations:
        out.append("| 核心创新 | " + " · ".join(innovations) + " |")
    if mc.get("architecture"):
        arch = mc["architecture"].replace("\n", " ").replace("|", "\\|")
        out.append(f"| 模型架构 | {arch} |")
    if datasets:
        ds = " · ".join(d.replace("|", "\\|") for d in datasets)
        out.append(f"| 数据集 | {ds} |")
    if mc.get("key_results"):
        kr = mc["key_results"].replace("\n", " ").replace("|", "\\|")
        out.append(f"| 关键结果 | {kr} |")
    out.append("")

    # Relevance to focus
    if row["relevance_to_focus"]:
        out.append("## 🎯 与本站重点领域的关联")
        out.append("")
        out.append(row["relevance_to_focus"])
        out.append("")

    # Snark
    if row["snark"]:
        out.append("## 💢 毒舌点评")
        out.append("")
        out.append(f"> {row['snark']}")
        out.append("")

    # Limitations
    if row["limitations"]:
        out.append("## ⚠️ 局限与未解决问题")
        out.append("")
        out.append(row["limitations"])
        out.append("")

    # Authors
    if row["authors"]:
        out.append("## 👥 作者")
        out.append("")
        out.append(f"<sub>{row['authors']}</sub>")
        out.append("")

    out.append("---")
    out.append("")
    out.append(f"评分：{row['score']:.1f}  |  "
               f"原始评分：{row['raw_score'] if row['raw_score'] is not None else row['score']:.1f}"
               f"{'  |  +1 重点领域加权' if _is_focus(row) else ''}")
    out.append("")
    out.append(f"[arxiv]({row['html_url']})  ·  [pdf]({row['pdf_url']})")
    out.append("")

    page_path.write_text("\n".join(out), encoding="utf-8")
    return slug


# --------------------------------------------------------------------------- daily digest


def render_for_date(date_str: str) -> Path | None:
    with connect() as conn:
        rows = papers_for_date(conn, date_str)
    if not rows:
        print(f"[render] no analyzed papers for {date_str}")
        return None

    rows = sorted(rows, key=lambda r: (r["score"] or 0), reverse=True)

    # daily directory (page bundle)
    daily_dir = POSTS_DIR / date_str
    daily_dir.mkdir(parents=True, exist_ok=True)
    daily_url = f"/posts/{date_str}/"

    # write per-paper pages first; remember slug + row
    paper_entries: list[tuple[str, "sqlite3.Row"]] = []
    for row in rows:
        slug = _render_paper_page(row, daily_dir, daily_url)
        paper_entries.append((slug, row))

    # daily index (index.md inside the bundle directory)
    counter = Counter(r["main_task"] or "#其他" for r in rows)
    top_dirs = counter.most_common(8)
    max_n = max(n for _, n in top_dirs) if top_dirs else 1

    # Daily front-matter tags: only main_task per paper (avoid tag explosion).
    main_tasks = sorted({r["main_task"] for r in rows if r["main_task"]})
    front_tags = main_tasks
    title = f"语音/音频论文速递 {date_str}"

    focus_rows = [(s, r) for s, r in paper_entries if _is_focus(r)]
    other_rows = [(s, r) for s, r in paper_entries if not _is_focus(r)]

    out: list[str] = []
    out.append("---")
    out.append(f'title: "{title}"')
    out.append(f'date: {date_str}T09:00:00+08:00')
    out.append("draft: false")
    out.append('categories: ["每日速递"]')
    out.append("tags: " + json.dumps(front_tags, ensure_ascii=False))
    out.append(f'summary: "今日共分析 {len(rows)} 篇论文，'
               f'其中 {len(focus_rows)} 篇为本站重点关注领域。"')
    out.append("ShowToc: true")
    out.append("---")
    out.append("")
    out.append(f"共分析 **{len(rows)}** 篇论文 · "
               f"重点领域 **{len(focus_rows)}** 篇")
    out.append("")

    out.append("## ⚡ 今日概览")
    out.append("")
    out.append("| 方向 | 数量 | 分布 |")
    out.append("| --- | --- | --- |")
    for tag, n in top_dirs:
        out.append(f"| {tag} | {n}篇 | {_bar(n, max_n)} |")
    out.append("")

    if focus_rows:
        out.append("## 🎯 本站重点领域")
        out.append("")
        out.append("> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离")
        out.append("")
        out.append("| 排名 | 论文 | 评分 | 主任务 |")
        out.append("| --- | --- | --- | --- |")
        for i, (slug, r) in enumerate(focus_rows):
            title_short = (r["title"] or "")[:60]
            out.append(
                f"| {_rank_marker(i)} | [{title_short}]({slug}/) | "
                f"{r['score']:.1f}分 | {r['main_task'] or ''} |"
            )
        out.append("")

    out.append("## 📊 完整排行榜（按评分降序）")
    out.append("")
    out.append("| 排名 | 论文 | 评分 | 分档 | 主任务 |")
    out.append("| --- | --- | --- | --- | --- |")
    for i, (slug, r) in enumerate(paper_entries):
        title_short = (r["title"] or "")[:55] + (
            "…" if r["title"] and len(r["title"]) > 55 else ""
        )
        focus_marker = " 🎯" if _is_focus(r) else ""
        out.append(
            f"| {_rank_marker(i)} | [{title_short}]({slug}/){focus_marker} | "
            f"{r['score']:.1f}分 | {r['tier'] or _percentile_bucket(r['score'])} | "
            f"{r['main_task'] or ''} |"
        )
    out.append("")

    out.append("## 📋 论文卡片速览")
    out.append("")
    for i, (slug, r) in enumerate(paper_entries):
        marker = _rank_marker(i)
        focus_marker = " 🎯" if _is_focus(r) else ""
        out.append(f"### {marker} [{r['title']}]({slug}/){focus_marker}")
        out.append("")
        out.append(
            f"**{r['score']:.1f}/10** · "
            f"{r['tier'] or _percentile_bucket(r['score'])} · "
            f"{r['main_task'] or ''}"
        )
        out.append("")
        if r["tldr"]:
            out.append(f"> {r['tldr']}")
            out.append("")
        if r["snark"]:
            out.append(f"💢 {r['snark']}")
            out.append("")
        out.append(f"[详情 →]({slug}/) · [arxiv]({r['html_url']})")
        out.append("")
        out.append("---")
        out.append("")

    md = "\n".join(out)
    index_path = daily_dir / "index.md"
    index_path.write_text(md, encoding="utf-8")
    print(f"[render] wrote {index_path} ({len(rows)} papers, "
          f"{len(focus_rows)} focus)")
    return index_path


def main() -> None:
    today = datetime.now(timezone.utc).astimezone().date().isoformat()
    render_for_date(today)


if __name__ == "__main__":
    main()
