"""Generate weekly / monthly leaderboards from the paper index."""
from __future__ import annotations
import json
from datetime import datetime, timezone, timedelta, date
from pathlib import Path

from config import RANKINGS_DIR
from db import connect, papers_in_range


def _table(rows) -> list[str]:
    out = ["| 排名 | 论文 | 评分 | 分档 | 主任务 |",
           "| --- | --- | --- | --- | --- |"]
    medals = ["🥇", "🥈", "🥉"]
    for i, r in enumerate(rows):
        marker = medals[i] if i < 3 else f"{i + 1}."
        title = (r["title"] or "")[:60]
        out.append(
            f"| {marker} | [{title}]({r['html_url']}) | "
            f"{(r['score'] or 0):.1f}分 | {r['tier'] or ''} | "
            f"{r['main_task'] or ''} |"
        )
    return out


def write_weekly(today: date | None = None) -> Path | None:
    today = today or datetime.now(timezone.utc).date()
    # Only emit on Mondays (weekday() == 0)
    if today.weekday() != 0:
        return None
    end = today - timedelta(days=1)
    start = end - timedelta(days=6)

    with connect() as conn:
        rows = papers_in_range(conn, start.isoformat(), end.isoformat(), limit=30)
    if not rows:
        return None

    iso_year, iso_week, _ = end.isocalendar()
    title = f"周排行榜 {iso_year}-W{iso_week:02d}"
    body = ["---",
            f'title: "{title}"',
            f'date: {today.isoformat()}T10:00:00+08:00',
            'draft: false',
            'categories: ["排行榜", "周榜"]',
            f'summary: "{start} ~ {end} 的高分论文"',
            "---",
            "",
            f"区间：**{start}** ~ **{end}**，共筛选 {len(rows)} 篇高分论文。",
            ""]
    body.extend(_table(rows))
    path = RANKINGS_DIR / f"weekly-{iso_year}-W{iso_week:02d}.md"
    path.write_text("\n".join(body), encoding="utf-8")
    print(f"[rankings] weekly -> {path}")
    return path


def write_monthly(today: date | None = None) -> Path | None:
    today = today or datetime.now(timezone.utc).date()
    # Only emit on day 1 of each month
    if today.day != 1:
        return None
    last_month_end = today - timedelta(days=1)
    start = last_month_end.replace(day=1)
    end = last_month_end

    with connect() as conn:
        rows = papers_in_range(conn, start.isoformat(), end.isoformat(), limit=50)
    if not rows:
        return None

    title = f"月排行榜 {start.year}-{start.month:02d}"
    body = ["---",
            f'title: "{title}"',
            f'date: {today.isoformat()}T10:00:00+08:00',
            'draft: false',
            'categories: ["排行榜", "月榜"]',
            f'summary: "{start} ~ {end} 的高分论文"',
            "---",
            "",
            f"区间：**{start}** ~ **{end}**，共 {len(rows)} 篇。",
            ""]
    body.extend(_table(rows))
    path = RANKINGS_DIR / f"monthly-{start.year}-{start.month:02d}.md"
    path.write_text("\n".join(body), encoding="utf-8")
    print(f"[rankings] monthly -> {path}")
    return path


def main() -> None:
    write_weekly()
    write_monthly()


if __name__ == "__main__":
    main()
