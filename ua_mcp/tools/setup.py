"""Setup and health tools."""

from __future__ import annotations

from typing import Any

from ..client_factory import get_config
from ..config import masked_api_key
from ..tool_contract import READ_ONLY_TOOL, tool_response


def register_setup_tools(mcp: object) -> None:
    """Register setup verification tools."""

    @mcp.tool(annotations=READ_ONLY_TOOL, structured_output=True)
    def ua_check_setup() -> dict[str, Any]:
        """Validate local env configuration required for Universal Ads MCP."""
        config = get_config()
        return tool_response(
            {
                "ready": True,
                "base_url": config.base_url,
                "api_key_tail": masked_api_key(config.api_key),
            }
        )
