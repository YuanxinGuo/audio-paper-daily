"""Build the site home page (`content/_index.md`) with live dashboard data:

  * today's stats (paper count, focus count, top score)
  * a hero card highlighting today's top paper
  * the last 5 focus-area papers across all days
"""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path

from config import SITE_DIR, FOCUS_TAGS, site_url
from db import (connect, papers_for_date, papers_recent_focus,
                latest_post_date)


HOME_PATH = SITE_DIR / "content" / "_index.md"


def _safe_json(s, default):
    if s is None:
        return default
    try:
        return json.loads(s) if s else default
    except Exception:
        return default


def main() -> None:
    with connect() as conn:
        latest = latest_post_date(conn)
        today_rows = papers_for_date(conn, latest) if latest else []
        focus_recent = papers_recent_focus(conn, FOCUS_TAGS, limit=5)

    today_rows = sorted(today_rows, key=lambda r: r["score"] or 0, reverse=True)
    top = today_rows[0] if today_rows else None
    focus_count = sum(
        1 for r in today_rows
        if (r["main_task"] in FOCUS_TAGS) or
           (set(_safe_json(r["tags"], [])) & FOCUS_TAGS)
    )

    out: list[str] = []
    out.append("---")
    out.append('title: "语音/音频论文速递"')
    out.append('description: "每日自动追踪语音与音频 AI 前沿论文，DeepSeek 深度分析"')
    out.append("---")
    out.append("")

    # ─── Hero ────────────────────────────────────────────────────────────
    out.append('<div class="hero">')
    out.append('<div class="hero-headline">')
    out.append('<span class="hero-badge">🎧 Daily Digest</span>')
    out.append('<h1 class="hero-title">语音 / 音频论文 <span class="grad">速递</span></h1>')
    out.append('<p class="hero-sub">每天自动从 arXiv eess.AS / cs.SD 抓取最新研究，'
               '由 DeepSeek 深度阅读、打分、提炼。</p>')
    out.append('<p class="hero-focus-tags">')
    out.append('<span class="focus-pill">语音增强</span>')
    out.append('<span class="focus-pill">目标说话人提取</span>')
    out.append('<span class="focus-pill">语音分离</span>')
    out.append('<span class="focus-pill">双耳音频</span>')
    out.append('<span class="focus-pill">乐器分离</span>')
    out.append('</p>')
    out.append('</div>')

    if top and latest:
        url = site_url(f"posts/{latest}/")
        out.append('<div class="hero-pick">')
        out.append('<div class="pick-label">今日一言推荐</div>')
        out.append(f'<div class="pick-score">{top["score"]:.1f}</div>')
        out.append(f'<a class="pick-title" href="{url}">{top["title"]}</a>')
        if top["tldr"]:
            out.append(f'<div class="pick-tldr">{top["tldr"]}</div>')
        out.append(f'<div class="pick-meta">'
                   f'<span class="tag-pill">{top["main_task"]}</span>'
                   f'<span>· {latest}</span></div>')
        out.append('</div>')
    out.append('</div>')
    out.append("")

    # ─── Stats dashboard ─────────────────────────────────────────────────
    if today_rows:
        out.append('<div class="dashboard">')
        out.append(f'<div class="stat-card"><div class="stat-num">{len(today_rows)}</div>'
                   f'<div class="stat-label">今日抽取</div></div>')
        out.append(f'<div class="stat-card stat-focus"><div class="stat-num">{focus_count}</div>'
                   f'<div class="stat-label">重点领域</div></div>')
        out.append(f'<div class="stat-card stat-top"><div class="stat-num">{top["score"]:.1f}</div>'
                   f'<div class="stat-label">最高分</div></div>')
        out.append(f'<div class="stat-card"><div class="stat-num">{latest}</div>'
                   f'<div class="stat-label">最近更新</div></div>')
        out.append('</div>')
        out.append("")
        out.append(f'<p class="dashboard-cta"><a href="{site_url(f"posts/{latest}/")}" class="btn-primary">'
                   f'查看 {latest} 完整速递 →</a></p>')
        out.append("")

    # ─── Recent focus papers ─────────────────────────────────────────────
    if focus_recent:
        out.append("## 🎯 重点领域最新")
        out.append("")
        out.append("> 跨日聚合：你亲选的 5 个领域里最近被分析的论文")
        out.append("")
        for r in focus_recent:
            date_str = (r["fetch_date"] or "")[:10]
            # build slug like render.py does
            from render import _slugify
            slug = _slugify(r["title"]) + "-" + r["arxiv_id"].replace(".", "-")
            url = site_url(f"posts/{date_str}/{slug}/")
            tldr = r["tldr"] or ""
            out.append(f'<div class="paper-card paper-card-focus">')
            out.append(f'<div class="card-rank">⭐</div>')
            out.append(f'<div class="card-body">')
            out.append(f'<a class="card-title" href="{url}">{r["title"]}</a>')
            out.append(f'<div class="card-meta">')
            out.append(f'<span class="card-score">{r["score"]:.1f}</span>')
            out.append(f'<span class="tag-pill">{r["main_task"]}</span>')
            out.append(f'<span class="card-date">{date_str}</span>')
            out.append(f'</div>')
            if tldr:
                out.append(f'<div class="card-tldr">{tldr}</div>')
            out.append(f'</div>')
            out.append(f'</div>')
        out.append("")

    # ─── About strip ─────────────────────────────────────────────────────
    out.append("## 关于本站")
    out.append("")
    out.append("- 数据源：[arXiv](https://arxiv.org/) eess.AS / cs.SD")
    out.append("- 分析模型：DeepSeek `deepseek-chat`")
    out.append("- 自动化：GitHub Actions（每日 09:00 北京时间）")
    out.append("- 源码：<https://github.com/YuanxinGuo/audio-paper-daily>")
    out.append("")
    out.append("> 评分由大语言模型基于摘要自动生成，仅供快速筛选。"
               "请始终回到原文做最终判断。")

    HOME_PATH.write_text("\n".join(out), encoding="utf-8")
    print(f"[home] wrote {HOME_PATH}")


if __name__ == "__main__":
    main()
