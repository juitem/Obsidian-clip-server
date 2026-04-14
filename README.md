# Obsidian Clip Server

Flask-based web clipping server for Obsidian. Clips web pages using trafilatura and/or Playwright, saves as markdown with frontmatter, and optionally pushes to Obsidian via Local REST API.

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install chromium
```

## Usage

```bash
# Set Obsidian Local REST API key
export OBSIDIAN_API_KEY="your-key-here"

# Start
./start-background.sh

# Stop
./stop.sh

# Status
./status.sh
```

Access at `http://localhost:7676` or remotely via Tailscale.

## API

```
POST /clip
{
  "url": "https://example.com/article",
  "methods": ["trafilatura", "playwright"],
  "obsidian": true
}
```

## Requirements

- Python 3
- Obsidian with [Local REST API](https://github.com/coddingtonbear/obsidian-local-rest-api) plugin (port 27123)
