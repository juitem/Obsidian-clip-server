import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env")

VAULT_PATH = os.environ["VAULT_PATH"]

SAVE_PATHS = {
    "trafilatura": os.path.join(VAULT_PATH, "ClippingsOthers", "trafilatura"),
    "playwright": os.path.join(VAULT_PATH, "ClippingsOthers", "playwright"),
}

OBSIDIAN_API_URL = "http://localhost:27123"
OBSIDIAN_API_KEY = os.environ.get("OBSIDIAN_API_KEY", "")

PORT = int(os.environ.get("PORT", 7676))
HOST = "0.0.0.0"

PLAYWRIGHT_TIMEOUT = 30000  # ms
MIN_CONTENT_LENGTH = 200
