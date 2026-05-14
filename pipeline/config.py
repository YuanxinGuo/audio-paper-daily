"""Project-wide configuration."""
from __future__ import annotations
from pathlib import Path
import os

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
SITE_DIR = ROOT / "site"
POSTS_DIR = SITE_DIR / "content" / "posts"
RANKINGS_DIR = SITE_DIR / "content" / "rankings"
DB_PATH = DATA_DIR / "papers.sqlite"

DATA_DIR.mkdir(parents=True, exist_ok=True)
POSTS_DIR.mkdir(parents=True, exist_ok=True)
RANKINGS_DIR.mkdir(parents=True, exist_ok=True)

# arxiv categories to monitor (speech / audio focused)
ARXIV_CATEGORIES = ["eess.AS", "cs.SD"]
ARXIV_MAX_RESULTS = 200  # per fetch
ARXIV_LOOKBACK_HOURS = 36  # tolerate cron drift

# HuggingFace daily papers
# Strong audio/speech keywords. Must contain at least one to be considered relevant.
HF_KEYWORDS = [
    "speech", "audio", "voice", "music", "acoustic", "sound",
    "tts", "asr", "song", "singing", "phoneme", "wav", "spectrogram",
    "vocal", "speaker", "auditory", "ultrasonic", "asr", "tts",
    "podcast", "transcription", "voice cloning", "voice conversion",
    "audio-visual", "audiovisual", "speech-to-text", "text-to-speech",
]

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
}
