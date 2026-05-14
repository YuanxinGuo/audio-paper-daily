"""Fetch recent papers from arxiv eess.AS / cs.SD."""
from __future__ import annotations
import time
from datetime import datetime, timedelta, timezone
from xml.etree import ElementTree as ET

import feedparser
import requests
from tenacity import retry, stop_after_attempt, wait_exponential

from config import ARXIV_CATEGORIES, ARXIV_MAX_RESULTS, ARXIV_LOOKBACK_HOURS
from db import connect, upsert_paper

ARXIV_API = "http://export.arxiv.org/api/query"


@retry(stop=stop_after_attempt(5), wait=wait_exponential(min=5, max=60))
def _query(start: int = 0) -> str:
    cat_query = "+OR+".join(f"cat:{c}" for c in ARXIV_CATEGORIES)
    params = (
        f"search_query={cat_query}"
        f"&sortBy=submittedDate&sortOrder=descending"
        f"&start={start}&max_results={ARXIV_MAX_RESULTS}"
    )
    url = f"{ARXIV_API}?{params}"
    # arxiv requests a descriptive UA and politeness; sleep before each call.
    time.sleep(3)
    r = requests.get(
        url,
        timeout=60,
        headers={"User-Agent": "audio-paper-daily/1.0 (+https://github.com/YuanxinGuo/audio-paper-daily)"},
    )
    r.raise_for_status()
    return r.text


def _normalize_id(entry_id: str) -> str:
    # http://arxiv.org/abs/2401.12345v1 -> 2401.12345
    raw = entry_id.rsplit("/", 1)[-1]
    return raw.split("v")[0]


def fetch() -> int:
    cutoff = datetime.now(timezone.utc) - timedelta(hours=ARXIV_LOOKBACK_HOURS)
    text = _query()
    feed = feedparser.parse(text)
    inserted = 0
    now_iso = datetime.now(timezone.utc).isoformat()

    with connect() as conn:
        for entry in feed.entries:
            published = datetime(*entry.published_parsed[:6], tzinfo=timezone.utc)
            if published < cutoff:
                continue

            arxiv_id = _normalize_id(entry.id)
            authors = ", ".join(a.name for a in getattr(entry, "authors", []))
            paper = {
                "arxiv_id": arxiv_id,
                "title": entry.title.strip().replace("\n", " "),
                "abstract": entry.summary.strip().replace("\n", " "),
                "authors": authors,
                "pub_date": published.date().isoformat(),
                "fetch_date": now_iso,
                "source": "arxiv",
                "pdf_url": f"https://arxiv.org/pdf/{arxiv_id}",
                "html_url": f"https://arxiv.org/abs/{arxiv_id}",
            }
            if upsert_paper(conn, paper):
                inserted += 1
    print(f"[arxiv] fetched={len(feed.entries)} new={inserted}")
    return inserted


if __name__ == "__main__":
    fetch()
