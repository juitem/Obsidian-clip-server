import os
import re
import unicodedata
from datetime import date

from config import SAVE_PATHS


def _slugify(text, max_length=60):
    """Convert text to a URL-friendly slug."""
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[-\s]+", "-", text).strip("-")
    return text[:max_length]


def save_clipping(title, url, content, method):
    """Save clipping as a markdown file with frontmatter.

    Returns the absolute file path and the vault-relative path.
    """
    today = date.today().isoformat()
    slug = _slugify(title)
    suffix = "-pw" if method == "playwright" else ""
    filename = f"{today}-{slug}{suffix}.md"

    save_dir = SAVE_PATHS[method]
    os.makedirs(save_dir, exist_ok=True)
    filepath = os.path.join(save_dir, filename)

    frontmatter = (
        f"---\n"
        f"title: \"{title}\"\n"
        f"source: \"{url}\"\n"
        f"date: {today}\n"
        f"method: {method}\n"
        f"---\n\n"
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(frontmatter + content)

    vault_relative = os.path.relpath(filepath, os.path.dirname(SAVE_PATHS["trafilatura"]).replace("/trafilatura", ""))
    # vault-relative path from vault root
    from config import VAULT_PATH
    vault_relative = os.path.relpath(filepath, VAULT_PATH)

    return filepath, vault_relative
