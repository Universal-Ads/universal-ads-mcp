"""Campaign endpoint tools."""

from __future__ import annotations

from typing import Any

from .. import api
from ..tool_contract import READ_ONLY_TOOL, tool_response


def register_campaign_tools(mcp: object) -> None:
    @mcp.tool(annotations=READ_ONLY_TOOL, structured_output=True)
    def ua_get_campaigns(
        adaccount_id: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
        sort: str | None = None,
        filters: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """List campaigns with optional filters."""
        extra_filters = filters or {}
        return tool_response(
            api.call(
                "get_campaigns",
                adaccount_id=adaccount_id,
                limit=limit,
                offset=offset,
                sort=sort,
                **extra_filters,
            )
        )

    @mcp.tool(annotations=READ_ONLY_TOOL, structured_output=True)
    def ua_get_campaign(campaign_id: str) -> dict[str, Any]:
        """Fetch one campaign by ID."""
        return tool_response(api.call("get_campaign", campaign_id=campaign_id))
