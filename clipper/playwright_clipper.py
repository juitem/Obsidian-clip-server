import asyncio

from markdownify import markdownify as md
from playwright.async_api import async_playwright

from config import PLAYWRIGHT_TIMEOUT

SELECTORS = ["main", "article", ".content", "body"]


async def _clip_async(url):
    """Fetch URL with headless Chromium and convert to markdown."""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url, wait_until="networkidle", timeout=PLAYWRIGHT_TIMEOUT)

        title = await page.title() or "Untitled"

        html = None
        for selector in SELECTORS:
            el = await page.query_selector(selector)
            if el:
                html = await el.inner_html()
                break

        await browser.close()

    if not html:
        raise ValueError("No content found on page")

    content = md(html, heading_style="ATX", strip=["script", "style"])
    return title, content.strip()


def clip(url):
    """Synchronous wrapper for async playwright clipping."""
    return asyncio.run(_clip_async(url))
