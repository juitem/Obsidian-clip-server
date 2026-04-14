import os
import sys
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env")

_REQUIRED = {
    "VAULT_PATH": "Obsidian vault directory (e.g. /Users/you/Documents/MyVault)",
}

_missing = [f"  {k}: {desc}" for k, desc in _REQUIRED.items() if not os.environ.get(k)]
if _missing:
    print("ERROR: Required environment variables not set:")
    print("\n".join(_missing))
    print("\nCopy .env.example to .env and fill in the values.")
    sys.exit(1)

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
