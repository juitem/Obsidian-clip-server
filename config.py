import os

VAULT_PATH = "/Users/juitem/Documents/ObsidianM4mini"

SAVE_PATHS = {
    "trafilatura": os.path.join(VAULT_PATH, "ClippingsOthers", "trafilatura"),
    "playwright": os.path.join(VAULT_PATH, "ClippingsOthers", "playwright"),
}

OBSIDIAN_API_URL = "http://localhost:27123"
OBSIDIAN_API_KEY = os.environ.get("OBSIDIAN_API_KEY", "")

PORT = 7676
HOST = "0.0.0.0"

PLAYWRIGHT_TIMEOUT = 30000  # ms
MIN_CONTENT_LENGTH = 200
