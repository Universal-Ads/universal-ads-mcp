"""Tool registration entrypoint."""

from __future__ import annotations

from .ad import register_ad_tools
from .adset import register_adset_tools
from .campaign import register_campaign_tools
from .creative import register_creative_tools
from .me import register_me_tools
from .media import register_media_tools
from .pixel import register_pixel_tools
from .report import register_report_tools
from .segment import register_segment_tools
from .setup import register_setup_tools


def register_tools(mcp: object) -> None:
    """Register all read-only MCP tools."""
    register_setup_tools(mcp)
    register_me_tools(mcp)
    register_campaign_tools(mcp)
    register_adset_tools(mcp)
    register_ad_tools(mcp)
    register_creative_tools(mcp)
    register_media_tools(mcp)
    register_report_tools(mcp)
    register_segment_tools(mcp)
    register_pixel_tools(mcp)
