import requests
import trafilatura

from config import MIN_CONTENT_LENGTH


def clip(url):
    """Fetch URL and extract content using trafilatura."""
    resp = requests.get(url, timeout=30, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0.0.0 Safari/537.36"
    })
    resp.raise_for_status()

    result = trafilatura.extract(
        resp.text,
        output_format="markdown",
        include_links=True,
        include_images=True,
        include_tables=True,
    )

    if not result or len(result) < MIN_CONTENT_LENGTH:
        raise ValueError(
            f"Extraction too short ({len(result) if result else 0} chars, "
            f"minimum {MIN_CONTENT_LENGTH})"
        )

    title = trafilatura.extract(resp.text, output_format="txt", only_with_metadata=False)
    metadata = trafilatura.metadata.extract_metadata(resp.text)
    title = metadata.title if metadata and metadata.title else url.split("/")[-1] or "Untitled"

    return title, result
