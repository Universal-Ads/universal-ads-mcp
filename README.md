## Universal Ads Read-Only MCP

Python FastMCP server exposing read-only Universal Ads SDK operations for local AI desktop clients.

If you download the MCP files to `jdoe/Documents/ua_mcp`, your `{path_to_mcp_directory}` is `jdoe/Documents/ua_mcp`.

## Prerequisites

- Python `>=3.11`
- [Poetry](https://python-poetry.org/)

## Setup

```bash
cd {path_to_mcp_directory}
poetry install
```

Obtain app credentials via Universal Ads Developer UI and store:

```bash
UNIVERSAL_ADS_API_KEY="your_api_key"
UNIVERSAL_ADS_PRIVATE_KEY="-----BEGIN EC PRIVATE KEY-----\\n...\\n-----END EC PRIVATE KEY-----"
```

## Run with Claude Desktop/Claude Code/Gemini CLI

NOTE: Mac users may be prompted to enable Python to access your documents and must accept for MCP functionality.

```json
{
  "mcpServers": {
    "universal-ads": {
      "command": "poetry",
      "args": [
        "--directory",
        "{path_to_mcp_directory}",
        "run",
        "ua-mcp"
      ],
      "env": {
        "UNIVERSAL_ADS_API_KEY": "YOUR_KEY",
        "UNIVERSAL_ADS_PRIVATE_KEY": "-----BEGIN EC PRIVATE KEY-----\\n...\\n-----END EC PRIVATE KEY-----"
      }
    }
  }
}
```


## Run Locally


```bash
EXPORT UNIVERSAL_ADS_API_KEY="your_api_key"
EXPORT UNIVERSAL_ADS_PRIVATE_KEY="-----BEGIN EC PRIVATE KEY-----\\n...\\n-----END EC PRIVATE KEY-----"
cd {path_to_mcp_directory}
poetry run ua-mcp
```

## Available resources

- `ua://setup`
- `ua://tool-catalog`
- `ua://privacy-and-safety`

## Quality checks

```bash
poetry run black --check .
poetry run pytest
poetry run python scripts/check_parity.py
```
