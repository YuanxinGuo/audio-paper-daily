"""Render today's analyzed papers into Hugo content.

Output layout:
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


def _safe_json(s, default):
    if s is None:
        return default
    try:
        return json.loads(s) if s else default
    except Exception:
        return default


def _star_rating(score: float) -> str:
    """Convert 0-10 to a five-star visualisation."""
    n = max(0, min(5, round(score / 2)))
    return "★" * n + "☆" * (5 - n)


# --------------------------------------------------------------------------- per-paper page


def _format_authors(row) -> str:
    """Build a markdown line:  *first* · co · co · co · ...· (and N more)."""
    authors_str = row["authors"] or ""
    if not authors_str:
        return ""
    all_authors = [a.strip() for a in authors_str.split(",") if a.strip()]
    first_set = set(_safe_json(row["first_authors"], []))
    corr_set = set(_safe_json(row["corresponding_authors"], []))

    out = []
    for a in all_authors[:8]:
        if a in first_set and a in corr_set:
            out.append(f"**{a}**\u2009¹\u2009✉")
        elif a in first_set:
            out.append(f"**{a}**\u2009¹")
        elif a in corr_set:
            out.append(f"{a}\u2009✉")
        else:
            out.append(a)
    extra = len(all_authors) - 8
    if extra > 0:
        out.append(f"… 等 {extra} 人")
    return " · ".join(out)


def _resource_buttons(row) -> str:
    """Return a markdown HTML row of resource buttons."""
    res = _safe_json(row["resources"], {})
    btns = []
    arxiv_id = row["arxiv_id"]
    btns.append(
        f'<a class="rsrc rsrc-arxiv" href="{row["html_url"]}" target="_blank" '
        f'rel="noopener">📄 arXiv</a>'
    )
    btns.append(
        f'<a class="rsrc rsrc-pdf" href="{row["pdf_url"]}" target="_blank" '
        f'rel="noopener">📑 PDF</a>'
    )
    if res.get("code_url"):
        btns.append(
            f'<a class="rsrc rsrc-code" href="{res["code_url"]}" target="_blank" '
            f'rel="noopener">💻 代码</a>'
        )
    if res.get("hf_url"):
        btns.append(
            f'<a class="rsrc rsrc-hf" href="{res["hf_url"]}" target="_blank" '
            f'rel="noopener">🤗 HuggingFace</a>'
        )
    if res.get("project_url"):
        btns.append(
            f'<a class="rsrc rsrc-proj" href="{res["project_url"]}" target="_blank" '
            f'rel="noopener">🌐 项目主页</a>'
        )
    if res.get("demo_url"):
        btns.append(
            f'<a class="rsrc rsrc-demo" href="{res["demo_url"]}" target="_blank" '
            f'rel="noopener">🔊 Demo</a>'
        )
    return '<div class="resources">' + "".join(btns) + "</div>"


def _bibtex(row) -> str:
    arxiv_id = row["arxiv_id"]
    first_author = (
        (_safe_json(row["first_authors"], []) or [""])[0]
        or (row["authors"] or "").split(",")[0]
        or "Unknown"
    ).split()[-1]
    year = (row["pub_date"] or "")[:4] or "2026"
    title = row["title"] or ""
    cite_key = f"{first_author.lower()}{year}{arxiv_id.split('.')[0]}"
    return (
        f"@article{{{cite_key},\n"
        f"  title  = {{{title}}},\n"
        f"  author = {{{(row['authors'] or '').replace(',', ' and ')}}},\n"
        f"  journal = {{arXiv preprint arXiv:{arxiv_id}}},\n"
        f"  year   = {{{year}}}\n"
        f"}}"
    )


def _render_paper_page(row, daily_dir: Path, daily_url: str) -> str:
    """Write a per-paper markdown file. Returns its slug for the index."""
    slug = _slugify(row["title"]) + "-" + row["arxiv_id"].replace(".", "-")
    page_path = daily_dir / f"{slug}.md"

    mc = _safe_json(row["model_card"], {})
    innovations = mc.get("innovations") or []
    datasets = mc.get("datasets") or []
    tags = _safe_json(row["tags"], [])
    affiliations = _safe_json(row["affiliations"], [])
    main_task = row["main_task"] or ""

    front_tags_for_yaml = sorted({main_task, *tags} - {""})

    rec_label = {
        "must_read": "🔥 强烈推荐通读",
        "optional":  "⏳ 按需阅读",
        "skip":      "✋ 可以跳过",
    }.get((row["recommendation"] or "optional"), "⏳ 按需阅读")

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
    out.append("TocOpen: false")
    out.append("---")
    out.append("")

    # ─── Hero card with score + meta ─────────────────────────────────────
    focus_class = " hero-focus" if _is_focus(row) else ""
    out.append(f'<div class="paper-hero{focus_class}">')
    out.append('<div class="hero-score">')
    out.append(f'<div class="score-num">{row["score"]:.1f}</div>')
    out.append(f'<div class="score-stars">{_star_rating(row["score"])}</div>')
    out.append(f'<div class="score-tier">{row["tier"] or _percentile_bucket(row["score"])}</div>')
    out.append('</div>')
    out.append('<div class="hero-meta">')
    out.append(f'<div class="meta-row"><span class="meta-key">主任务</span>'
               f'<span class="meta-val tag-pill">{main_task}</span></div>')
    if tags:
        tag_pills = " ".join(f'<span class="tag-pill tag-pill-soft">{t}</span>' for t in tags)
        out.append(f'<div class="meta-row"><span class="meta-key">标签</span>'
                   f'<span class="meta-val">{tag_pills}</span></div>')
    out.append(f'<div class="meta-row"><span class="meta-key">arXiv</span>'
               f'<span class="meta-val mono">{row["arxiv_id"]}</span></div>')
    out.append(f'<div class="meta-row"><span class="meta-key">发布</span>'
               f'<span class="meta-val">{row["pub_date"] or row["fetch_date"][:10]}</span></div>')
    out.append(f'<div class="meta-row"><span class="meta-key">建议</span>'
               f'<span class="meta-val">{rec_label}</span></div>')
    if _is_focus(row):
        out.append('<div class="meta-row"><span class="meta-key">⭐</span>'
                   '<span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>')
    out.append('</div>')
    out.append('</div>')
    out.append("")

    # ─── Resources row ───────────────────────────────────────────────────
    out.append(_resource_buttons(row))
    out.append("")

    # ─── TL;DR ───────────────────────────────────────────────────────────
    if row["tldr"]:
        out.append('<div class="tldr-box">')
        out.append(f'<span class="tldr-tag">TL;DR</span>{row["tldr"]}')
        out.append('</div>')
        out.append("")

    # ─── Authors & affiliation card ──────────────────────────────────────
    out.append("## 👥 作者与机构")
    out.append("")
    authors_md = _format_authors(row)
    if authors_md:
        out.append(authors_md)
        out.append("")
    if affiliations:
        out.append("**机构**：" + " · ".join(affiliations))
        out.append("")
    out.append('<sub>¹ = 第一作者　✉ = 通讯作者</sub>')
    out.append("")

    # ─── Reading suggestion ──────────────────────────────────────────────
    if row["reading_suggestion"]:
        out.append("## 📖 阅读建议")
        out.append("")
        out.append(row["reading_suggestion"])
        out.append("")

    # ─── Model card ──────────────────────────────────────────────────────
    out.append("## 🧩 模型一栏概览")
    out.append("")
    out.append("| 项 | 内容 |")
    out.append("| --- | --- |")
    if mc.get("scenario"):
        out.append(f"| **应用场景** | {mc['scenario']} |")
    if innovations:
        out.append("| **核心创新** | " + " · ".join(innovations) + " |")
    if mc.get("architecture"):
        arch = mc["architecture"].replace("\n", " ").replace("|", "\\|")
        out.append(f"| **模型架构** | {arch} |")
    if datasets:
        ds = " · ".join(d.replace("|", "\\|") for d in datasets)
        out.append(f"| **数据集** | {ds} |")
    if mc.get("key_results"):
        kr = mc["key_results"].replace("\n", " ").replace("|", "\\|")
        out.append(f"| **关键结果** | {kr} |")
    out.append("")

    # ─── Open-source resources detailed list ─────────────────────────────
    res = _safe_json(row["resources"], {})
    has_extras = any([
        res.get("code_url"), res.get("hf_url"),
        res.get("project_url"), res.get("demo_url"),
        res.get("dataset_urls"),
    ])
    if has_extras:
        out.append("## 🔗 开源资源")
        out.append("")
        if res.get("code_url"):
            out.append(f"- **代码**：<{res['code_url']}>")
        if res.get("hf_url"):
            out.append(f"- **HuggingFace**：<{res['hf_url']}>")
        if res.get("project_url"):
            out.append(f"- **项目主页**：<{res['project_url']}>")
        if res.get("demo_url"):
            out.append(f"- **Demo / 试听**：<{res['demo_url']}>")
        for u in res.get("dataset_urls", []):
            out.append(f"- **数据集**：<{u}>")
        out.append("")

    # ─── Relevance to focus ──────────────────────────────────────────────
    if row["relevance_to_focus"]:
        out.append("## 🎯 与本站重点领域的关联")
        out.append("")
        out.append(row["relevance_to_focus"])
        out.append("")

    # ─── Limitations ─────────────────────────────────────────────────────
    if row["limitations"]:
        out.append("## ⚠️ 局限与未解决问题")
        out.append("")
        out.append(row["limitations"])
        out.append("")

    # ─── BibTeX ──────────────────────────────────────────────────────────
    out.append("## 📋 引用")
    out.append("")
    out.append("```bibtex")
    out.append(_bibtex(row))
    out.append("```")
    out.append("")

    # ─── Footer ──────────────────────────────────────────────────────────
    out.append("---")
    out.append("")
    out.append(
        f'<div class="paper-footer">'
        f'<span>评分：{row["score"]:.1f}</span>'
        f'<span>原始：{(row["raw_score"] if row["raw_score"] is not None else row["score"]):.1f}</span>'
        f'{"<span>+1 重点领域加权</span>" if _is_focus(row) else ""}'
        f'<a href="{daily_url}">← 返回 {row["fetch_date"][:10]} 速递</a>'
        f'</div>'
    )
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

    daily_dir = POSTS_DIR / date_str
    daily_dir.mkdir(parents=True, exist_ok=True)
    daily_url = f"/posts/{date_str}/"

    paper_entries: list[tuple[str, "sqlite3.Row"]] = []
    for row in rows:
        slug = _render_paper_page(row, daily_dir, daily_url)
        paper_entries.append((slug, row))

    counter = Counter(r["main_task"] or "#其他" for r in rows)
    top_dirs = counter.most_common(8)
    max_n = max(n for _, n in top_dirs) if top_dirs else 1

    main_tasks = sorted({r["main_task"] for r in rows if r["main_task"]})
    front_tags = main_tasks
    title = f"语音/音频论文速递 {date_str}"

    focus_rows = [(s, r) for s, r in paper_entries if _is_focus(r)]
    top_paper = paper_entries[0][1] if paper_entries else None

    out: list[str] = []
    out.append("---")
    out.append(f'title: "{title}"')
    out.append(f'date: {date_str}T09:00:00+08:00')
    out.append("draft: false")
    out.append('categories: ["每日速递"]')
    out.append("tags: " + json.dumps(front_tags, ensure_ascii=False))
    out.append(f'summary: "今日 {len(rows)} 篇 · 重点领域 {len(focus_rows)} 篇 · '
               f'最高分 {top_paper["score"]:.1f}（{top_paper["main_task"]}）"')
    out.append("ShowToc: false")
    out.append("---")
    out.append("")

    # ─── Daily summary card ──────────────────────────────────────────────
    out.append('<div class="daily-stats">')
    out.append(f'<div class="stat-card"><div class="stat-num">{len(rows)}</div>'
               f'<div class="stat-label">分析论文</div></div>')
    out.append(f'<div class="stat-card stat-focus"><div class="stat-num">{len(focus_rows)}</div>'
               f'<div class="stat-label">重点领域</div></div>')
    out.append(f'<div class="stat-card stat-top"><div class="stat-num">{top_paper["score"]:.1f}</div>'
               f'<div class="stat-label">最高分</div></div>')
    out.append('</div>')
    out.append("")

    out.append("## ⚡ 今日方向分布")
    out.append("")
    out.append("| 方向 | 数量 | 分布 |")
    out.append("| --- | --- | --- |")
    for tag, n in top_dirs:
        out.append(f"| {tag} | {n}篇 | `{_bar(n, max_n)}` |")
    out.append("")

    if focus_rows:
        out.append("## 🎯 本站重点领域")
        out.append("")
        out.append("> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离")
        out.append("")
        for slug, r in focus_rows:
            tldr = r["tldr"] or ""
            out.append(f'<div class="paper-card paper-card-focus">')
            out.append(f'<div class="card-rank">⭐</div>')
            out.append(f'<div class="card-body">')
            out.append(f'<a class="card-title" href="{slug}/">{r["title"]}</a>')
            out.append(f'<div class="card-meta">')
            out.append(f'<span class="card-score">{r["score"]:.1f}</span>')
            out.append(f'<span class="tag-pill">{r["main_task"]}</span>')
            out.append(f'</div>')
            if tldr:
                out.append(f'<div class="card-tldr">{tldr}</div>')
            out.append(f'</div>')
            out.append(f'</div>')
        out.append("")

    out.append("## 📊 完整排行榜")
    out.append("")
    out.append("| 排名 | 论文 | 评分 | 主任务 |")
    out.append("| --- | --- | --- | --- |")
    for i, (slug, r) in enumerate(paper_entries):
        title_short = (r["title"] or "")[:60] + (
            "…" if r["title"] and len(r["title"]) > 60 else ""
        )
        focus_marker = " 🎯" if _is_focus(r) else ""
        out.append(
            f"| {_rank_marker(i)} | [{title_short}]({slug}/){focus_marker} | "
            f"**{r['score']:.1f}** | {r['main_task'] or ''} |"
        )
    out.append("")

    out.append("## 📋 论文卡片速览")
    out.append("")
    for i, (slug, r) in enumerate(paper_entries):
        marker = _rank_marker(i)
        focus_marker = ' <span class="focus-mark">🎯</span>' if _is_focus(r) else ""
        out.append(f'<div class="paper-card">')
        out.append(f'<div class="card-rank">{marker}</div>')
        out.append(f'<div class="card-body">')
        out.append(f'<a class="card-title" href="{slug}/">{r["title"]}</a>{focus_marker}')
        out.append(f'<div class="card-meta">')
        out.append(f'<span class="card-score">{r["score"]:.1f}</span>')
        out.append(f'<span class="tag-pill">{r["main_task"]}</span>')
        out.append(f'<span class="card-tier">{r["tier"] or _percentile_bucket(r["score"])}</span>')
        out.append(f'</div>')
        if r["tldr"]:
            out.append(f'<div class="card-tldr">{r["tldr"]}</div>')
        out.append(f'<div class="card-action">')
        out.append(f'<a href="{slug}/">详情 →</a> · '
                   f'<a href="{r["html_url"]}" target="_blank" rel="noopener">arXiv</a>')
        out.append(f'</div>')
        out.append(f'</div>')
        out.append(f'</div>')
    out.append("")

    md = "\n".join(out)
    # IMPORTANT: must be `_index.md` (section index), NOT `index.md` (page bundle).
    # With `index.md` Hugo treats sibling .md files as bundle resources, not pages.
    index_path = daily_dir / "_index.md"
    index_path.write_text(md, encoding="utf-8")
    # Clean up legacy index.md if present (from earlier broken runs).
    legacy = daily_dir / "index.md"
    if legacy.exists():
        legacy.unlink()
    print(f"[render] wrote {index_path} ({len(rows)} papers, "
          f"{len(focus_rows)} focus)")
    return index_path


def main() -> None:
    today = datetime.now(timezone.utc).astimezone().date().isoformat()
    render_for_date(today)


if __name__ == "__main__":
    main()
