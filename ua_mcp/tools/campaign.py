"""Campaign endpoint tools."""

from __future__ import annotations

from typing import Any

from .. import api
from ..tool_contract import READ_ONLY_TOOL, normalize_limit, tool_response


def register_campaign_tools(mcp: object) -> None:
    @mcp.tool(annotations=READ_ONLY_TOOL, structured_output=True)
    def ua_get_campaigns(
        adaccount_id: str,
        campaign_ids: list[str] | None = None,
        name: str | None = None,
        status: list[str] | None = None,
        campaign_type: str | None = None,
        include_archived: bool | None = None,
        limit: int | None = None,
        offset: int | None = None,
        sort: str | None = None,
    ) -> dict[str, Any]:
        """List campaigns for an ad account.

        status: optional list of statuses to filter by (e.g. ["active", "paused"]).
        limit: defaults to 10 when omitted (TPA range 1-100).
        """
        effective_limit = normalize_limit(limit=limit, default_limit=10, max_limit=100)
        return tool_response(
            api.call(
                "get_campaigns",
                adaccount_id=adaccount_id,
                campaign_ids=campaign_ids,
                name=name,
                status=status,
                campaign_type=campaign_type,
                include_archived=include_archived,
                limit=effective_limit,
                offset=offset,
                sort=sort,
            )
        )

    @mcp.tool(annotations=READ_ONLY_TOOL, structured_output=True)
    def ua_get_campaign(campaign_id: str) -> dict[str, Any]:
        """Fetch one campaign by ID."""
        return tool_response(api.call("get_campaign", campaign_id=campaign_id))
