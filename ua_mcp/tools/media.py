"""Media endpoint tools."""

from __future__ import annotations

from typing import Any

from .. import api
from ..tool_contract import READ_ONLY_TOOL, tool_response


def register_media_tools(mcp: object) -> None:
    @mcp.tool(annotations=READ_ONLY_TOOL, structured_output=True)
    def ua_get_media(media_id: str) -> dict[str, Any]:
        """Fetch one media record by ID."""
        return tool_response(api.call("get_media", media_id=media_id))
