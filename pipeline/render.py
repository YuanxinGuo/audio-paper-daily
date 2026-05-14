"""Render today's analyzed papers into a Hugo markdown post."""
from __future__ import annotations
import json
from collections import Counter
from datetime import datetime, timezone, timedelta
from pathlib import Path

from config import POSTS_DIR
from db import connect, papers_for_date

MEDALS = ["🥇", "🥈", "🥉"]


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


def _highlights_to_md(highlights_json: str) -> str:
    try:
        items = json.loads(highlights_json or "[]")
    except Exception:
        items = []
    if not items:
        return ""
    return "\n".join(f"- {h}" for h in items)


def _tags_to_md(tags_json: str) -> str:
    try:
        tags = json.loads(tags_json or "[]")
    except Exception:
        tags = []
    return " ".join(tags)


def render_for_date(date_str: str) -> Path | None:
    with connect() as conn:
        rows = papers_for_date(conn, date_str)
    if not rows:
        print(f"[render] no analyzed papers for {date_str}")
        return None

    rows = sorted(rows, key=lambda r: (r["score"] or 0), reverse=True)

    # main_task distribution
    counter = Counter(r["main_task"] or "#其他" for r in rows)
    top_dirs = counter.most_common(8)
    max_n = max(n for _, n in top_dirs) if top_dirs else 1

    # collect all tags for front matter
    all_tags: set[str] = set()
    for r in rows:
        try:
            all_tags.update(json.loads(r["tags"] or "[]"))
        except Exception:
            pass
        if r["main_task"]:
            all_tags.add(r["main_task"])

    front_tags = sorted(all_tags)
    title = f"语音/音频论文速递 {date_str}"

    out: list[str] = []
    out.append("---")
    out.append(f'title: "{title}"')
    out.append(f'date: {date_str}T09:00:00+08:00')
    out.append("draft: false")
    out.append("categories: [\"每日速递\"]")
    out.append("tags: " + json.dumps(front_tags, ensure_ascii=False))
    out.append(f'summary: "今日共分析 {len(rows)} 篇论文。"')
    out.append("---")
    out.append("")
    out.append(f"共分析 **{len(rows)}** 篇论文")
    out.append("")
    out.append("## ⚡ 今日概览")
    out.append("")
    out.append(f"📥 抓取 {len(rows)} 篇 → 🔬 深度分析完成")
    out.append("")
    out.append("## 🏷️ 热门方向")
    out.append("")
    out.append("| 方向 | 数量 | 分布 |")
    out.append("| --- | --- | --- |")
    for tag, n in top_dirs:
        out.append(f"| {tag} | {n}篇 | {_bar(n, max_n)} |")
    out.append("")
    out.append(f"## 📊 论文评分排行榜（{len(rows)} 篇，按分数降序）")
    out.append("")
    out.append("| 排名 | 论文 | 评分 | 分档 | 主任务 |")
    out.append("| --- | --- | --- | --- | --- |")
    for i, r in enumerate(rows):
        title_short = (r["title"] or "")[:55] + (
            "…" if r["title"] and len(r["title"]) > 55 else ""
        )
        out.append(
            f"| {_rank_marker(i)} | {title_short} | "
            f"{r['score']:.1f}分 | {r['tier'] or _percentile_bucket(r['score'])} | "
            f"{r['main_task'] or ''} |"
        )
    out.append("")
    out.append("## 📋 论文列表")
    out.append("")
    for i, r in enumerate(rows):
        marker = _rank_marker(i)
        out.append(f"### {marker} {r['title']}")
        out.append("")
        out.append(
            f"**{r['score']:.1f}/10** · {r['tier'] or _percentile_bucket(r['score'])} · "
            f"{r['main_task'] or ''} · {_tags_to_md(r['tags'])}"
        )
        out.append("")
        if r["tldr"]:
            out.append(f"> {r['tldr']}")
            out.append("")
        hl = _highlights_to_md(r["highlights"])
        if hl:
            out.append("**亮点**")
            out.append("")
            out.append(hl)
            out.append("")
        if r["method"]:
            out.append(f"**方法**：{r['method']}")
            out.append("")
        if r["results"]:
            out.append(f"**结论**：{r['results']}")
            out.append("")
        if r["limitations"]:
            out.append(f"**局限**：{r['limitations']}")
            out.append("")
        if r["authors"]:
            out.append(f"<sub>作者：{r['authors']}</sub>")
            out.append("")
        out.append(f"[arxiv]({r['html_url']}) · [pdf]({r['pdf_url']})")
        out.append("")
        out.append("---")
        out.append("")

    md = "\n".join(out)
    path = POSTS_DIR / f"{date_str}.md"
    path.write_text(md, encoding="utf-8")
    print(f"[render] wrote {path} ({len(rows)} papers)")
    return path


def main() -> None:
    today = datetime.now(timezone.utc).astimezone().date().isoformat()
    render_for_date(today)


if __name__ == "__main__":
    main()
