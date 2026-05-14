"""Fetch recent papers from arxiv eess.AS / cs.SD.

Strategy: try RSS first (less rate-limited, returns the day's listing),
fall back to the API if RSS fails. Network errors NEVER abort the pipeline.
"""
from __future__ import annotations
import time
from datetime import datetime, timedelta, timezone

import feedparser
import requests
from tenacity import retry, stop_after_attempt, wait_exponential

from config import ARXIV_CATEGORIES, ARXIV_MAX_RESULTS, ARXIV_LOOKBACK_HOURS
from db import connect, upsert_paper

ARXIV_API = "http://export.arxiv.org/api/query"
ARXIV_RSS = "http://export.arxiv.org/rss"
USER_AGENT = (
    "audio-paper-daily/1.0 "
    "(+https://github.com/YuanxinGuo/audio-paper-daily; bot@example.com)"
)


@retry(stop=stop_after_attempt(4), wait=wait_exponential(min=5, max=60))
def _fetch_rss(category: str) -> str:
    url = f"{ARXIV_RSS}/{category}"
    time.sleep(3)
    r = requests.get(url, timeout=60, headers={"User-Agent": USER_AGENT})
    r.raise_for_status()
    return r.text


@retry(stop=stop_after_attempt(4), wait=wait_exponential(min=5, max=60))
def _fetch_api() -> str:
    cat_query = "+OR+".join(f"cat:{c}" for c in ARXIV_CATEGORIES)
    params = (
        f"search_query={cat_query}"
        f"&sortBy=submittedDate&sortOrder=descending"
        f"&start=0&max_results={ARXIV_MAX_RESULTS}"
    )
    url = f"{ARXIV_API}?{params}"
    time.sleep(3)
    r = requests.get(url, timeout=60, headers={"User-Agent": USER_AGENT})
    r.raise_for_status()
    return r.text


def _normalize_id(entry_id: str) -> str:
    raw = entry_id.rsplit("/", 1)[-1]
    return raw.split("v")[0]


def _from_rss() -> list[dict]:
    """Returns list of paper dicts (no fetch_date set)."""
    out: list[dict] = []
    for cat in ARXIV_CATEGORIES:
        try:
            text = _fetch_rss(cat)
        except Exception as e:
            print(f"[arxiv] RSS {cat} failed: {e}")
            continue
        feed = feedparser.parse(text)
        for entry in feed.entries:
            arxiv_id = _normalize_id(entry.link)
            out.append({
                "arxiv_id": arxiv_id,
                "title": entry.title.strip().replace("\n", " "),
                "abstract": (
                    getattr(entry, "summary", "") or ""
                ).strip().replace("\n", " "),
                "authors": getattr(entry, "author", "") or "",
                "pub_date": datetime.now(timezone.utc).date().isoformat(),
                "source": "arxiv-rss",
            })
        # be polite between categories
        time.sleep(2)
    return out


def _from_api() -> list[dict]:
    text = _fetch_api()
    feed = feedparser.parse(text)
    cutoff = datetime.now(timezone.utc) - timedelta(hours=ARXIV_LOOKBACK_HOURS)
    out: list[dict] = []
    for entry in feed.entries:
        published = datetime(*entry.published_parsed[:6], tzinfo=timezone.utc)
        if published < cutoff:
            continue
        arxiv_id = _normalize_id(entry.id)
        authors = ", ".join(a.name for a in getattr(entry, "authors", []))
        out.append({
            "arxiv_id": arxiv_id,
            "title": entry.title.strip().replace("\n", " "),
            "abstract": entry.summary.strip().replace("\n", " "),
            "authors": authors,
            "pub_date": published.date().isoformat(),
            "source": "arxiv-api",
        })
    return out


def fetch() -> int:
    """Best-effort fetch. Never raises."""
    now_iso = datetime.now(timezone.utc).isoformat()
    items: list[dict] = []
    try:
        items = _from_rss()
        print(f"[arxiv] RSS yielded {len(items)} entries")
    except Exception as e:
        print(f"[arxiv] RSS path crashed entirely: {e}")

    if not items:
        try:
            items = _from_api()
            print(f"[arxiv] API yielded {len(items)} entries")
        except Exception as e:
            print(f"[arxiv] API path failed: {e}")
            return 0

    inserted = 0
    with connect() as conn:
        for it in items:
            it["fetch_date"] = now_iso
            it["pdf_url"] = f"https://arxiv.org/pdf/{it['arxiv_id']}"
            it["html_url"] = f"https://arxiv.org/abs/{it['arxiv_id']}"
            if upsert_paper(conn, it):
                inserted += 1
    print(f"[arxiv] new={inserted}")
    return inserted


if __name__ == "__main__":
    fetch()
