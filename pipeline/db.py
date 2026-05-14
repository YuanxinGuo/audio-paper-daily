"""SQLite-backed paper index."""
from __future__ import annotations
import sqlite3
import json
from contextlib import contextmanager
from typing import Iterable, Optional

from config import DB_PATH


SCHEMA = """
CREATE TABLE IF NOT EXISTS papers (
  arxiv_id    TEXT PRIMARY KEY,
  title       TEXT NOT NULL,
  abstract    TEXT NOT NULL,
  authors     TEXT,
  pub_date    TEXT,
  fetch_date  TEXT NOT NULL,
  source      TEXT NOT NULL,
  pdf_url     TEXT,
  html_url    TEXT,
  -- analysis
  score       REAL,
  tier        TEXT,
  main_task   TEXT,
  tags        TEXT,    -- JSON array
  tldr        TEXT,
  highlights  TEXT,    -- JSON array
  method      TEXT,
  results     TEXT,
  limitations TEXT,
  analyzed_at TEXT
);

CREATE INDEX IF NOT EXISTS idx_fetch_date ON papers(fetch_date);
CREATE INDEX IF NOT EXISTS idx_score      ON papers(score);
CREATE INDEX IF NOT EXISTS idx_pub_date   ON papers(pub_date);
"""


@contextmanager
def connect():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        conn.executescript(SCHEMA)
        yield conn
        conn.commit()
    finally:
        conn.close()


def upsert_paper(conn: sqlite3.Connection, paper: dict) -> bool:
    """Insert if new. Returns True if inserted, False if already existed."""
    cur = conn.execute(
        "SELECT 1 FROM papers WHERE arxiv_id = ?", (paper["arxiv_id"],)
    )
    if cur.fetchone():
        return False
    conn.execute(
        """
        INSERT INTO papers (arxiv_id, title, abstract, authors, pub_date,
                            fetch_date, source, pdf_url, html_url)
        VALUES (:arxiv_id, :title, :abstract, :authors, :pub_date,
                :fetch_date, :source, :pdf_url, :html_url)
        """,
        paper,
    )
    return True


def get_unanalyzed(conn: sqlite3.Connection) -> list[sqlite3.Row]:
    return list(conn.execute(
        "SELECT * FROM papers WHERE analyzed_at IS NULL ORDER BY fetch_date DESC"
    ))


def save_analysis(conn: sqlite3.Connection, arxiv_id: str, analysis: dict) -> None:
    conn.execute(
        """
        UPDATE papers SET
          score=:score, tier=:tier, main_task=:main_task,
          tags=:tags, tldr=:tldr, highlights=:highlights,
          method=:method, results=:results, limitations=:limitations,
          analyzed_at=datetime('now')
        WHERE arxiv_id=:arxiv_id
        """,
        {
            "arxiv_id": arxiv_id,
            "score": analysis.get("score"),
            "tier": analysis.get("tier"),
            "main_task": analysis.get("main_task"),
            "tags": json.dumps(analysis.get("tags", []), ensure_ascii=False),
            "tldr": analysis.get("tldr"),
            "highlights": json.dumps(analysis.get("highlights", []),
                                    ensure_ascii=False),
            "method": analysis.get("method"),
            "results": analysis.get("results"),
            "limitations": analysis.get("limitations"),
        },
    )


def papers_for_date(conn: sqlite3.Connection, date_str: str) -> list[sqlite3.Row]:
    return list(conn.execute(
        """
        SELECT * FROM papers
        WHERE date(fetch_date) = date(?) AND analyzed_at IS NOT NULL
        ORDER BY score DESC
        """,
        (date_str,),
    ))


def papers_in_range(conn: sqlite3.Connection,
                    start: str, end: str,
                    limit: int = 50) -> list[sqlite3.Row]:
    return list(conn.execute(
        """
        SELECT * FROM papers
        WHERE date(fetch_date) BETWEEN date(?) AND date(?)
          AND analyzed_at IS NOT NULL
        ORDER BY score DESC
        LIMIT ?
        """,
        (start, end, limit),
    ))
