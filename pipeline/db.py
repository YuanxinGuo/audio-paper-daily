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
  -- analysis (legacy)
  score          REAL,
  tier           TEXT,
  main_task      TEXT,
  tags           TEXT,    -- JSON array
  tldr           TEXT,
  highlights     TEXT,    -- JSON array
  method         TEXT,
  results        TEXT,
  limitations    TEXT,
  analyzed_at    TEXT,
  -- analysis (extended)
  raw_score          REAL,
  reading_suggestion TEXT,
  model_card         TEXT,    -- JSON object
  relevance_to_focus TEXT,
  snark              TEXT,    -- legacy, no longer used
  recommendation     TEXT,    -- must_read | optional | skip
  -- academic metadata
  first_authors          TEXT,   -- JSON array
  corresponding_authors  TEXT,   -- JSON array
  affiliations           TEXT,   -- JSON array
  resources              TEXT    -- JSON object
);

CREATE INDEX IF NOT EXISTS idx_fetch_date ON papers(fetch_date);
CREATE INDEX IF NOT EXISTS idx_score      ON papers(score);
CREATE INDEX IF NOT EXISTS idx_pub_date   ON papers(pub_date);
"""

# Idempotent migrations for older DB files.
MIGRATIONS = [
    "ALTER TABLE papers ADD COLUMN raw_score REAL",
    "ALTER TABLE papers ADD COLUMN reading_suggestion TEXT",
    "ALTER TABLE papers ADD COLUMN model_card TEXT",
    "ALTER TABLE papers ADD COLUMN relevance_to_focus TEXT",
    "ALTER TABLE papers ADD COLUMN snark TEXT",
    "ALTER TABLE papers ADD COLUMN recommendation TEXT",
    "ALTER TABLE papers ADD COLUMN first_authors TEXT",
    "ALTER TABLE papers ADD COLUMN corresponding_authors TEXT",
    "ALTER TABLE papers ADD COLUMN affiliations TEXT",
    "ALTER TABLE papers ADD COLUMN resources TEXT",
]


def _run_migrations(conn: sqlite3.Connection) -> None:
    for stmt in MIGRATIONS:
        try:
            conn.execute(stmt)
        except sqlite3.OperationalError:
            pass  # column already exists


@contextmanager
def connect():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        conn.executescript(SCHEMA)
        _run_migrations(conn)
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
    mc = analysis.get("model_card") or {}
    conn.execute(
        """
        UPDATE papers SET
          score=:score, raw_score=:raw_score, tier=:tier, main_task=:main_task,
          tags=:tags, tldr=:tldr,
          highlights=:highlights,
          method=:method, results=:results, limitations=:limitations,
          reading_suggestion=:reading_suggestion,
          model_card=:model_card,
          relevance_to_focus=:relevance_to_focus,
          recommendation=:recommendation,
          first_authors=:first_authors,
          corresponding_authors=:corresponding_authors,
          affiliations=:affiliations,
          resources=:resources,
          analyzed_at=datetime('now')
        WHERE arxiv_id=:arxiv_id
        """,
        {
            "arxiv_id": arxiv_id,
            "score": analysis.get("score"),
            "raw_score": analysis.get("raw_score"),
            "tier": analysis.get("tier"),
            "main_task": analysis.get("main_task"),
            "tags": json.dumps(analysis.get("tags", []), ensure_ascii=False),
            "tldr": analysis.get("tldr"),
            "highlights": json.dumps(mc.get("innovations", []),
                                     ensure_ascii=False),
            "method": mc.get("architecture"),
            "results": mc.get("key_results"),
            "limitations": analysis.get("limitations"),
            "reading_suggestion": analysis.get("reading_suggestion"),
            "model_card": json.dumps(mc, ensure_ascii=False),
            "relevance_to_focus": analysis.get("relevance_to_focus"),
            "recommendation": analysis.get("recommendation"),
            "first_authors": json.dumps(
                analysis.get("first_authors") or [], ensure_ascii=False),
            "corresponding_authors": json.dumps(
                analysis.get("corresponding_authors") or [], ensure_ascii=False),
            "affiliations": json.dumps(
                analysis.get("affiliations") or [], ensure_ascii=False),
            "resources": json.dumps(
                analysis.get("resources") or {}, ensure_ascii=False),
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


def papers_recent_focus(conn: sqlite3.Connection,
                        focus_tags: set[str],
                        limit: int = 5) -> list[sqlite3.Row]:
    """Return the N most recent analyzed papers whose main_task is in focus_tags."""
    placeholders = ",".join("?" * len(focus_tags))
    return list(conn.execute(
        f"""
        SELECT * FROM papers
        WHERE analyzed_at IS NOT NULL
          AND main_task IN ({placeholders})
        ORDER BY date(fetch_date) DESC, score DESC
        LIMIT ?
        """,
        (*focus_tags, limit),
    ))


def latest_post_date(conn: sqlite3.Connection) -> str | None:
    row = conn.execute(
        "SELECT date(fetch_date) FROM papers "
        "WHERE analyzed_at IS NOT NULL ORDER BY fetch_date DESC LIMIT 1"
    ).fetchone()
    return row[0] if row else None
