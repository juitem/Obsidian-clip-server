import subprocess
import time

import psutil
import requests

from config import OBSIDIAN_API_KEY, OBSIDIAN_API_URL


def _is_obsidian_running():
    """Check if Obsidian process is running."""
    for proc in psutil.process_iter(["name"]):
        if proc.info["name"] and "obsidian" in proc.info["name"].lower():
            return True
    return False


def _api_health_check():
    """Check if Obsidian Local REST API is responsive."""
    try:
        resp = requests.get(
            f"{OBSIDIAN_API_URL}/",
            headers={"Authorization": f"Bearer {OBSIDIAN_API_KEY}"},
            timeout=2,
        )
        return resp.status_code == 200
    except requests.RequestException:
        return False


def ensure_obsidian_running():
    """Ensure Obsidian is running and REST API is ready.

    Returns True if ready, raises RuntimeError on timeout.
    """
    if not _is_obsidian_running():
        subprocess.run(["open", "-a", "Obsidian"], check=True)

    for _ in range(60):
        if _api_health_check():
            return True
        time.sleep(1)

    raise RuntimeError("Obsidian Local REST API not responding after 60s")


def push_to_obsidian(vault_relative_path, content):
    """Push note to Obsidian via Local REST API.

    PUT /vault/{filepath}
    """
    ensure_obsidian_running()

    resp = requests.put(
        f"{OBSIDIAN_API_URL}/vault/{vault_relative_path}",
        headers={
            "Authorization": f"Bearer {OBSIDIAN_API_KEY}",
            "Content-Type": "text/markdown",
        },
        data=content.encode("utf-8"),
        timeout=10,
    )
    resp.raise_for_status()
    return True
