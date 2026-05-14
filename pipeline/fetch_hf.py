"""Fetch HuggingFace daily papers and keep only audio/speech-relevant ones."""
from __future__ import annotations
from datetime import datetime, timezone, timedelta

import requests
from tenacity import retry, stop_after_attempt, wait_exponential

from config import HF_KEYWORDS
from db import connect, upsert_paper

HF_API = "https://huggingface.co/api/daily_papers"


@retry(stop=stop_after_attempt(3), wait=wait_exponential(min=2, max=30))
def _query(date: str | None = None) -> list[dict]:
    params = {"date": date} if date else {}
    r = requests.get(HF_API, params=params, timeout=60,
                     headers={"User-Agent": "audio-paper-daily/1.0"})
    r.raise_for_status()
    return r.json()


def _is_relevant(text: str) -> bool:
    low = text.lower()
    return any(kw in low for kw in HF_KEYWORDS)


def fetch() -> int:
    inserted = 0
    now_iso = datetime.now(timezone.utc).isoformat()
    # Try today + yesterday so we don't miss the boundary.
    today = datetime.now(timezone.utc).date()
    dates = [today.isoformat(), (today - timedelta(days=1)).isoformat()]

    with connect() as conn:
        seen_total = 0
        for d in dates:
            try:
                items = _query(d)
            except Exception as e:
                print(f"[hf] query {d} failed: {e}")
                continue
            seen_total += len(items)
            for it in items:
                paper = it.get("paper", {})
                arxiv_id = paper.get("id") or it.get("id")
                if not arxiv_id:
                    continue
                title = paper.get("title", "").strip()
                abstract = paper.get("summary", "").strip()
                if not _is_relevant(f"{title} {abstract}"):
                    continue
                authors = ", ".join(
                    a.get("name", "") for a in paper.get("authors", [])
                )
                pub = paper.get("publishedAt", "")
                pub_date = pub[:10] if pub else d
                row = {
                    "arxiv_id": arxiv_id,
                    "title": title,
                    "abstract": abstract,
                    "authors": authors,
                    "pub_date": pub_date,
                    "fetch_date": now_iso,
                    "source": "hf",
                    "pdf_url": f"https://arxiv.org/pdf/{arxiv_id}",
                    "html_url": f"https://arxiv.org/abs/{arxiv_id}",
                }
                if upsert_paper(conn, row):
                    inserted += 1
    print(f"[hf] scanned={seen_total} new={inserted}")
    return inserted


if __name__ == "__main__":
    fetch()
