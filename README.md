# Universal Ads MCP (Read-Only)

A local Model Context Protocol (MCP) server that lets AI assistants (e.g. Claude Desktop, Cowork, Claude Code, Gemini CLI, and any other local MCP-compatible client) query your Universal Ads accounts. Enables read-only operations from the Universal Ads SDK: organizations, ad accounts, campaigns, ad sets, ads, creatives, media, pixels, segments, and reports.

The server runs locally and only makes outbound calls to the Universal Ads API.

## Prerequisites

- Python `>=3.11`
- [Poetry](https://python-poetry.org/)
- A Universal Ads Developer App (see below)

## Create a Universal Ads Developer App

1. Go to <https://developers.universalads.com/>.
2. Click **Log in / Sign up** and sign in with your Universal Ads credentials, or create a Universal Ads account.
3. Follow the prompts to create a Developer Account.
4. Create a new app dedicated to this MCP with only these scopes: **Ad read-only** and **Account read-only**.
5. Save the **App ID**, **API Key**, and **Private Key** securely. Treat the Private Key as a high-sensitivity password.
6. Once your new app is approved, grant it access to your Universal Ads Organization by following the instructions at <https://developers.universalads.com/#authorizing-adsmanager-access>.

## Install

Clone or download this repository. Throughout this README, `{path_to_mcp_directory}` refers to the directory you placed it in (e.g., `~/Documents/ua_mcp`).

```bash
cd {path_to_mcp_directory}
poetry install
```

Poetry creates a virtual environment, installs dependencies, and registers the `ua-mcp` command. First run takes a minute or two.

## Configure credentials

Copy `.env.example` to `.env` in the project root:

```bash
cp .env.example .env
```

Open `.env` and set:

```ini
UNIVERSAL_ADS_API_KEY=your_api_key

UNIVERSAL_ADS_PRIVATE_KEY="-----BEGIN EC PRIVATE KEY-----
...key body...
-----END EC PRIVATE KEY-----"
```

Multi-line PEM (shown above) and single-line with literal `\n` between lines are both accepted.

## Smoke test

Run the server directly to confirm credentials parse and the SDK initializes:

```bash
poetry run ua-mcp
```

A healthy run prints a couple of startup lines and then sits silently waiting on stdin; that's how MCP servers signal "ready." Press `Ctrl+C` to exit. If you see a `ValueError` about missing env vars or a key-parse error, jump to [Troubleshooting](#troubleshooting).

## Connect it to your MCP client

> **Use the absolute path to `poetry` in every config below.** MCP clients launch their server processes with a minimal environment and often can't resolve `poetry` from a bare name. Find it with `which poetry` — typically `/opt/homebrew/bin/poetry` or `~/.local/bin/poetry`.

### Claude Desktop / Cowork

Edit (or create) `~/Library/Application Support/Claude/claude_desktop_config.json` and merge in:

```json
{
  "mcpServers": {
    "universal-ads": {
      "command": "/ABSOLUTE/PATH/TO/poetry",
      "args": [
        "--directory",
        "/ABSOLUTE/PATH/TO/universal-ads-mcp",
        "run",
        "ua-mcp"
      ]
    }
  }
}
```

Then **fully quit and relaunch** the app — `⌘Q` or right-click the dock icon → Quit. Closing the window isn't enough.

Credentials stay in `.env`; nothing sensitive lives in the JSON config.

> **macOS:** The first time the server runs, you may be prompted to allow Python to access the folder you installed it in. Approve it — the server needs it to function.

### Claude Code

The simplest path is Claude Code's built-in command:

```bash
claude mcp add universal-ads /ABSOLUTE/PATH/TO/poetry \
  --directory /ABSOLUTE/PATH/TO/universal-ads-mcp \
  run ua-mcp
```

Confirm with `claude mcp list`.

### Gemini CLI

Edit `~/.gemini/settings.json` and add the same `mcpServers` block shown for Claude Desktop above. Restart the CLI session for changes to take effect.

## Windows notes

The instructions above work on Windows with these substitutions:

- **Find Poetry's absolute path:** use `where poetry` instead of `which poetry`. Typical result: `C:\Users\you\.local\bin\poetry.exe`.
- **Config file locations:**
  - Claude Desktop / Cowork: `%APPDATA%\Claude\claude_desktop_config.json`
  - Claude Code: `%USERPROFILE%\.claude.json`
  - Gemini CLI: `%USERPROFILE%\.gemini\settings.json`
- **Paths in JSON:** escape each backslash (`C:\\Users\\you\\universal-ads-mcp`) or use forward slashes (`C:/Users/you/universal-ads-mcp`).
- **Quit the app:** right-click the system tray icon → Quit. Closing the window isn't enough.
- **Run locally with PowerShell:**

powershell

```powershell
  $env:UNIVERSAL_ADS_API_KEY = "your_api_key"
  $env:UNIVERSAL_ADS_PRIVATE_KEY = "-----BEGIN EC PRIVATE KEY-----\n...\n-----END EC PRIVATE KEY-----"
  cd $env:USERPROFILE\Documents\ua_mcp
  poetry run ua-mcp
```

## Available resources

- `ua://setup` — installation and setup instructions
- `ua://tool-catalog` — machine-readable list of every tool the server exposes
- `ua://privacy-and-safety` — what the server does and doesn't do with your data

After you connect, ask your assistant for the full tool list — it will read `ua://tool-catalog` for you.

## Troubleshooting

**`poetry: command not found`** — Poetry isn't on your `PATH`. Run `pipx ensurepath`, then open a new terminal window. If it still fails, add Poetry's bin directory (typically `~/.local/bin`) to your shell config.

**`Missing required env var ...`** — The server can't find your credentials. Check that `.env` exists in the project root (same folder as `pyproject.toml`), variable names are spelled exactly, and the MCP client config points to the right `--directory`.

**PEM key errors (e.g., `Could not deserialize key data`)** — The private key isn't being passed cleanly. Make sure both `BEGIN`/`END` lines are present, the body is intact across line breaks, and (if using the single-line `\n` format) every newline is a literal backslash-n, not an actual line break.

**MCP client doesn't show `universal-ads`** — You forgot to fully quit/restart the app, the JSON config has a syntax error (validate with `python -m json.tool < /path/to/config.json`), or `command` is a bare `poetry` instead of an absolute path.

## Development

```bash
poetry run black --check .
poetry run pytest
poetry run python scripts/check_parity.py
```

## Privacy and safety

- The server only makes outbound calls to the Universal Ads API.
- Credentials are read from environment variables and `.env` only, never from chat.
- Every exposed operation is read-only. Create, update, delete, and upload SDK methods are deliberately not surfaced.
