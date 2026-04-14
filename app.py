import time
import traceback
from concurrent.futures import ThreadPoolExecutor

from flask import Flask, jsonify, render_template, request

import config
from clipper import trafilatura_clipper, playwright_clipper
from clipper.storage import save_clipping

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


def _run_clip(url, method):
    """Run a single clipping method. Returns a result dict."""
    start = time.time()
    try:
        if method == "trafilatura":
            title, content = trafilatura_clipper.clip(url)
        elif method == "playwright":
            title, content = playwright_clipper.clip(url)
        else:
            raise ValueError(f"Unknown method: {method}")

        filepath, _ = save_clipping(title, url, content, method)

        elapsed = round(time.time() - start, 2)
        return {
            "method": method,
            "success": True,
            "file": filepath,
            "elapsed": elapsed,
        }

    except Exception as e:
        elapsed = round(time.time() - start, 2)
        return {
            "method": method,
            "success": False,
            "error": str(e),
            "detail": traceback.format_exc(),
            "elapsed": elapsed,
        }


@app.route("/clip", methods=["POST"])
def clip():
    data = request.get_json()
    if not data or "url" not in data:
        return jsonify({"error": "Missing 'url' field"}), 400

    url = data["url"].strip()
    methods = [m for m in data.get("methods", ["trafilatura", "playwright"]) if m != "obsidian"]

    if not methods:
        return jsonify({"error": "No clipping method selected"}), 400

    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = {executor.submit(_run_clip, url, m): m for m in methods}
        results = [f.result() for f in futures]

    return jsonify({"results": results})


if __name__ == "__main__":
    app.run(host=config.HOST, port=config.PORT, debug=False)
