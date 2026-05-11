"""Static resources for MCP discoverability and policy."""

from __future__ import annotations

import json

TOOL_CATALOG = {
    "setup": ["ua_check_setup"],
    "me": ["ua_get_organizations", "ua_get_adaccounts"],
    "campaign": ["ua_get_campaigns", "ua_get_campaign"],
    "adset": ["ua_get_adsets", "ua_get_adset"],
    "ad": ["ua_get_ads", "ua_get_ad"],
    "creative": ["ua_get_creatives", "ua_get_creative"],
    "media": ["ua_get_media"],
    "report": [
        "ua_get_campaign_report",
        "ua_get_adset_report",
        "ua_get_ad_report",
    ],
    "audience": ["ua_get_audiences", "ua_get_audience"],
    "pixel": ["ua_get_pixels", "ua_get_pixel", "ua_get_pixel_events"],
}


def register_resources(mcp: object) -> None:
    """Register static resources for setup and policy guidance."""

    @mcp.resource("ua://setup", mime_type="text/markdown")
    def setup() -> str:
        return (
            "# Universal Ads MCP setup\n\n"
            "Set `UNIVERSAL_ADS_API_KEY` and `UNIVERSAL_ADS_PRIVATE_KEY` before starting the server. "
            "`UNIVERSAL_ADS_BASE_URL` is optional.\n\n"
            "Run locally with `poetry run ua-mcp`.\n"
        )

    @mcp.resource("ua://tool-catalog", mime_type="application/json")
    def tool_catalog() -> str:
        return json.dumps(TOOL_CATALOG, indent=2)

    @mcp.resource("ua://privacy-and-safety", mime_type="text/markdown")
    def privacy() -> str:
        return (
            "# Privacy and safety\n\n"
            "- This MCP server is read-only and does not expose delivery mutations.\n"
            "- Credential values are loaded from env vars and never accepted as tool inputs.\n"
            "- Sensitive fields such as `access_token`, `script`, and signed `result_url` are redacted by default.\n"
        )
