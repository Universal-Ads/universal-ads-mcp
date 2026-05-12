"""Audience endpoint tools."""

from __future__ import annotations

from typing import Any

from .. import api
from ..tool_contract import READ_ONLY_TOOL, normalize_limit, tool_response


def register_audience_tools(mcp: object) -> None:
    @mcp.tool(annotations=READ_ONLY_TOOL, structured_output=True)
    def ua_get_audiences(
        adaccount_id: str,
        name: str | None = None,
        description: str | None = None,
        status: str | None = None,
        audience_ids: list[str] | None = None,
        segment_ids: list[str] | None = None,
        segment_type: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
        sort: str | None = None,
    ) -> dict[str, Any]:
        """List audiences for an ad account. limit: defaults to 10 when omitted (TPA range 1-100)."""
        effective_limit = normalize_limit(limit=limit, default_limit=10, max_limit=100)
        return tool_response(
            api.call(
                "get_audiences",
                adaccount_id=adaccount_id,
                name=name,
                description=description,
                status=status,
                audience_ids=audience_ids,
                segment_ids=segment_ids,
                segment_type=segment_type,
                limit=effective_limit,
                offset=offset,
                sort=sort,
            )
        )

    @mcp.tool(annotations=READ_ONLY_TOOL, structured_output=True)
    def ua_get_audience(audience_id: str) -> dict[str, Any]:
        """Fetch one audience by ID."""
        return tool_response(api.call("get_audience", audience_id=audience_id))
