# Obsidian Clip Server

Flask-based web clipping server for Obsidian. Clips web pages using trafilatura and/or Playwright, saves as markdown directly to the vault.

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install chromium
```

Copy `.env.example` to `.env` and set `VAULT_PATH`:

```bash
cp .env.example .env
```

## Usage

```bash
# Start
./start-background.sh

# Stop
./stop.sh

# Status
./status.sh
```

Access at `http://localhost:7676` or remotely via Tailscale.

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `VAULT_PATH` | yes | Absolute path to Obsidian vault |
| `OBSIDIAN_API_KEY` | no | Obsidian Local REST API key (not needed for now) |
| `PORT` | no | Server port (default: 7676) |

## API

```
POST /clip
{
  "url": "https://example.com/article",
  "methods": ["trafilatura", "playwright"]
}
```

## Clipping Methods

| Method | How |
|--------|-----|
| trafilatura | HTTP fetch → trafilatura extract |
| playwright | Headless Chromium → markdownify |

## Requirements

- Python 3
- Obsidian vault accessible on the same machine
