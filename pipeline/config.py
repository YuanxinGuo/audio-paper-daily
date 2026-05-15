"""Project-wide configuration."""
from __future__ import annotations
from pathlib import Path
from urllib.parse import urlparse
import os
import re

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
SITE_DIR = ROOT / "site"
POSTS_DIR = SITE_DIR / "content" / "posts"
RANKINGS_DIR = SITE_DIR / "content" / "rankings"
DB_PATH = DATA_DIR / "papers.sqlite"

DATA_DIR.mkdir(parents=True, exist_ok=True)
POSTS_DIR.mkdir(parents=True, exist_ok=True)
RANKINGS_DIR.mkdir(parents=True, exist_ok=True)


def _read_base_path() -> str:
    """Extract the URL path prefix from site/config.toml's baseURL.

    For example, baseURL = "https://user.github.io/myrepo/" yields
    "/myrepo".  Returns "" for an apex domain.
    """
    cfg = SITE_DIR / "config.toml"
    if not cfg.exists():
        return ""
    text = cfg.read_text(encoding="utf-8")
    m = re.search(r'^\s*baseURL\s*=\s*"([^"]+)"', text, re.MULTILINE)
    if not m:
        return ""
    parsed = urlparse(m.group(1))
    path = parsed.path.rstrip("/")
    return path


# Path prefix for all internal links.  Hugo will auto-prepend this for
# Hugo-managed paths (e.g. .Permalink), but anything we hand-write in
# markdown / raw HTML must include it ourselves.
SITE_BASE_PATH = _read_base_path()


def site_url(path: str) -> str:
    """Build a site-internal URL by prepending the base path.

    Accepts paths like "posts/2026-05-15/" (with or without leading slash)
    and returns e.g. "/audio-paper-daily/posts/2026-05-15/".
    """
    if not path:
        return SITE_BASE_PATH + "/"
    if not path.startswith("/"):
        path = "/" + path
    return SITE_BASE_PATH + path

# arxiv categories to monitor (speech / audio focused)
ARXIV_CATEGORIES = ["eess.AS", "cs.SD"]
ARXIV_MAX_RESULTS = 200  # per fetch
ARXIV_LOOKBACK_HOURS = 36  # tolerate cron drift

# DeepSeek
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "")
DEEPSEEK_BASE_URL = "https://api.deepseek.com"
DEEPSEEK_MODEL = "deepseek-chat"
LLM_CONCURRENCY = 4
LLM_TIMEOUT = 90

# Tag canonicalisation: map synonyms to a canonical form so the
# tag cloud doesn't fragment.
TAG_ALIASES = {
    "#ASR": "#语音识别",
    "#TTS": "#语音合成",
    "#speech recognition": "#语音识别",
    "#speech synthesis": "#语音合成",
    "#音频生成": "#音频生成",
    "#sound event detection": "#音频事件检测",
    "#speech enhancement": "#语音增强",
    "#denoising": "#语音增强",
    "#dereverberation": "#语音增强",
    "#target speaker extraction": "#目标说话人提取",
    "#TSE": "#目标说话人提取",
    "#personalized speech enhancement": "#目标说话人提取",
    "#speech separation": "#语音分离",
    "#source separation": "#语音分离",
    "#binaural": "#双耳音频",
    "#binaural audio": "#双耳音频",
    "#spatial audio": "#双耳音频",
    "#HRTF": "#双耳音频",
    "#music source separation": "#乐器分离",
    "#MSS": "#乐器分离",
    "#stem separation": "#乐器分离",
}

# Topics the site cares about. A paper whose main_task or tags hits one of
# these gets a +SCORE_FOCUS_BONUS bump (capped at 10.0).
FOCUS_TAGS = {
    "#语音增强",
    "#目标说话人提取",
    "#语音分离",
    "#双耳音频",
    "#乐器分离",
}
SCORE_FOCUS_BONUS = 1.0

# Daily analysis budget: how many papers to analyse per run.
DAILY_ANALYSIS_LIMIT = 10

# Keyword pre-filter (lower-cased, English) for the title+abstract of an
# arxiv paper. Hits any keyword in any focus group → the paper is treated
# as a focus candidate and prioritised when filling the 10-slot quota.
FOCUS_KEYWORDS = {
    "#语音增强": [
        "speech enhancement", "speech denoising", "noise reduction",
        "dereverberation", "speech restoration", "noise suppression",
    ],
    "#目标说话人提取": [
        "target speaker extraction", "speaker extraction",
        "personalized speech enhancement", "voicefilter", "speakerbeam",
        "spex", "target speech",
    ],
    "#语音分离": [
        "speech separation", "source separation", "cocktail party",
        "speaker separation", "multi-speaker separation",
        "diarization and separation",
    ],
    "#双耳音频": [
        "binaural audio", "binaural rendering", "binaural synthesis",
        "spatial audio", "hrtf", "head-related transfer",
        "3d audio", "ambisonic",
    ],
    "#乐器分离": [
        "music source separation", "stem separation", "instrument separation",
        "vocal separation", "singing voice separation", "musdb",
    ],
}
