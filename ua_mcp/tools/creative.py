"""Creative endpoint tools."""

from __future__ import annotations

from typing import Any

from .. import api
from ..tool_contract import READ_ONLY_TOOL, tool_response


def register_creative_tools(mcp: object) -> None:
    @mcp.tool(annotations=READ_ONLY_TOOL, structured_output=True)
    def ua_get_creatives(
        adaccount_id: str | None = None,
        campaign_id: str | None = None,
        adset_id: str | None = None,
        ad_id: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
        sort: str | None = None,
    ) -> dict[str, Any]:
        """List creatives."""
        return tool_response(
            api.call(
                "get_creatives",
                adaccount_id=adaccount_id,
                campaign_id=campaign_id,
                adset_id=adset_id,
                ad_id=ad_id,
                limit=limit,
                offset=offset,
                sort=sort,
            )
        )

    @mcp.tool(annotations=READ_ONLY_TOOL, structured_output=True)
    def ua_get_creative(creative_id: str) -> dict[str, Any]:
        """Fetch one creative by ID."""
        return tool_response(api.call("get_creative", creative_id=creative_id))
