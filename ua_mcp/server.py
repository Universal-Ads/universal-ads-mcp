"""FastMCP entrypoint for Universal Ads read-only server."""

from __future__ import annotations

from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

from .client_factory import validate_startup_credentials
from .resources import register_resources
from .tools import register_tools

INSTRUCTIONS = """
Universal Ads MCP exposes read-only operations that map to UniversalAdsClient GET methods.
It does not expose create, update, delete, upload, verify, or schedule-report operations.
Credentials are loaded from environment variables only.
"""


def create_mcp() -> FastMCP:
    """Construct MCP app and register resources/tools."""
    mcp = FastMCP(
        "Universal Ads Read-Only MCP",
        instructions=INSTRUCTIONS.strip(),
        website_url="https://www.universalads.com/",
    )
    register_resources(mcp)
    register_tools(mcp)
    return mcp


def main() -> None:
    """Run server over stdio transport."""
    load_dotenv()
    validate_startup_credentials()
    app = create_mcp()
    app.run(transport="stdio")


if __name__ == "__main__":
    main()
