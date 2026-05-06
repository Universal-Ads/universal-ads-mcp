"""Pixel endpoint tools."""

from __future__ import annotations

from typing import Any

from .. import api
from ..tool_contract import READ_ONLY_TOOL, tool_response


def register_pixel_tools(mcp: object) -> None:
    @mcp.tool(annotations=READ_ONLY_TOOL, structured_output=True)
    def ua_get_pixels(
        adaccount_id: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
        sort: str | None = None,
        filters: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """List pixels with optional filters."""
        extra_filters = filters or {}
        return tool_response(
            api.call(
                "get_pixels",
                adaccount_id=adaccount_id,
                limit=limit,
                offset=offset,
                sort=sort,
                **extra_filters,
            )
        )

    @mcp.tool(annotations=READ_ONLY_TOOL, structured_output=True)
    def ua_get_pixel(pixel_id: str) -> dict[str, Any]:
        """Fetch one pixel by ID."""
        return tool_response(api.call("get_pixel", pixel_id=pixel_id))

    @mcp.tool(annotations=READ_ONLY_TOOL, structured_output=True)
    def ua_get_pixel_events(
        pixel_id: str,
        limit: int | None = None,
        offset: int | None = None,
        filters: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """List pixel events."""
        extra_filters = filters or {}
        return tool_response(
            api.call(
                "get_pixel_events",
                pixel_id=pixel_id,
                limit=limit,
                offset=offset,
                **extra_filters,
            )
        )
