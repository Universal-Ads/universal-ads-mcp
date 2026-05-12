"""Adset endpoint tools."""

from __future__ import annotations

from typing import Any

from .. import api
from ..tool_contract import READ_ONLY_TOOL, normalize_limit, tool_response


def register_adset_tools(mcp: object) -> None:
    @mcp.tool(annotations=READ_ONLY_TOOL, structured_output=True)
    def ua_get_adsets(
        adaccount_id: str | None = None,
        campaign_id: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
        sort: str | None = None,
        filters: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """List ad sets with optional filters. limit: defaults to 10 when omitted (TPA range 1-100)."""
        extra_filters = filters or {}
        effective_limit = normalize_limit(limit=limit, default_limit=10, max_limit=100)
        return tool_response(
            api.call(
                "get_adsets",
                adaccount_id=adaccount_id,
                campaign_id=campaign_id,
                limit=effective_limit,
                offset=offset,
                sort=sort,
                **extra_filters,
            )
        )

    @mcp.tool(annotations=READ_ONLY_TOOL, structured_output=True)
    def ua_get_adset(adset_id: str) -> dict[str, Any]:
        """Fetch one ad set by ID."""
        return tool_response(api.call("get_adset", adset_id=adset_id))
