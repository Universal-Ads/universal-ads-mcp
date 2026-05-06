"""Segment endpoint tools."""

from __future__ import annotations

from typing import Any

from .. import api
from ..tool_contract import READ_ONLY_TOOL, tool_response


def register_segment_tools(mcp: object) -> None:
    @mcp.tool(annotations=READ_ONLY_TOOL, structured_output=True)
    def ua_get_segments(
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
        """List segments for an ad account."""
        return tool_response(
            api.call(
                "get_segments",
                adaccount_id=adaccount_id,
                name=name,
                description=description,
                status=status,
                audience_ids=audience_ids,
                segment_ids=segment_ids,
                segment_type=segment_type,
                limit=limit,
                offset=offset,
                sort=sort,
            )
        )

    @mcp.tool(annotations=READ_ONLY_TOOL, structured_output=True)
    def ua_get_segment(segment_id: str) -> dict[str, Any]:
        """Fetch one segment by ID."""
        return tool_response(api.call("get_segment", segment_id=segment_id))
