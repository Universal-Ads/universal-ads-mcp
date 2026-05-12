"""Adset endpoint tools."""

from __future__ import annotations

from typing import Any

from .. import api
from ..tool_contract import READ_ONLY_TOOL, normalize_limit, tool_response


def register_adset_tools(mcp: object) -> None:
    @mcp.tool(annotations=READ_ONLY_TOOL, structured_output=True)
    def ua_get_adsets(
        adaccount_id: str,
        campaign_ids: list[str] | None = None,
        adset_ids: list[str] | None = None,
        name: str | None = None,
        status: list[str] | None = None,
        include_archived: bool | None = None,
        limit: int | None = None,
        offset: int | None = None,
        sort: str | None = None,
    ) -> dict[str, Any]:
        """List ad sets for an ad account. limit: defaults to 10 when omitted (TPA range 1-100)."""
        effective_limit = normalize_limit(limit=limit, default_limit=10, max_limit=100)
        return tool_response(
            api.call(
                "get_adsets",
                adaccount_id=adaccount_id,
                campaign_ids=campaign_ids,
                adset_ids=adset_ids,
                name=name,
                status=status,
                include_archived=include_archived,
                limit=effective_limit,
                offset=offset,
                sort=sort,
            )
        )

    @mcp.tool(annotations=READ_ONLY_TOOL, structured_output=True)
    def ua_get_adset(adset_id: str) -> dict[str, Any]:
        """Fetch one ad set by ID."""
        return tool_response(api.call("get_adset", adset_id=adset_id))
