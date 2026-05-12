"""Ad endpoint tools."""

from __future__ import annotations

from typing import Any

from .. import api
from ..tool_contract import READ_ONLY_TOOL, normalize_limit, tool_response


def register_ad_tools(mcp: object) -> None:
    @mcp.tool(annotations=READ_ONLY_TOOL, structured_output=True)
    def ua_get_ads(
        adaccount_id: str,
        campaign_ids: list[str] | None = None,
        adset_ids: list[str] | None = None,
        ad_ids: list[str] | None = None,
        status: list[str] | None = None,
        include_archived: bool | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> dict[str, Any]:
        """List ads for an ad account. limit: defaults to 10 when omitted (TPA range 1-100)."""
        effective_limit = normalize_limit(limit=limit, default_limit=10, max_limit=100)
        return tool_response(
            api.call(
                "get_ads",
                adaccount_id=adaccount_id,
                campaign_ids=campaign_ids,
                adset_ids=adset_ids,
                ad_ids=ad_ids,
                status=status,
                include_archived=include_archived,
                limit=effective_limit,
                offset=offset,
            )
        )

    @mcp.tool(annotations=READ_ONLY_TOOL, structured_output=True)
    def ua_get_ad(ad_id: str) -> dict[str, Any]:
        """Fetch one ad by ID."""
        return tool_response(api.call("get_ad", ad_id=ad_id))
