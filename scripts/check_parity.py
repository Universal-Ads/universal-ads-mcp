"""Check MCP tool parity against SDK read-only methods."""

from __future__ import annotations

from ua_mcp.resources import TOOL_CATALOG

SDK_READ_METHODS = {
    "get_organizations",
    "get_adaccounts",
    "get_campaigns",
    "get_campaign",
    "get_adsets",
    "get_adset",
    "get_ads",
    "get_ad",
    "get_creatives",
    "get_creative",
    "get_media",
    "get_campaign_report",
    "get_adset_report",
    "get_ad_report",
    "get_scheduled_report",
    "get_segments",
    "get_segment",
    "get_pixels",
    "get_pixel",
    "get_pixel_events",
}


def _expected_tool_names() -> set[str]:
    return {f"ua_{method}" for method in SDK_READ_METHODS}


def _catalog_tool_names() -> set[str]:
    names: set[str] = set()
    for group_tools in TOOL_CATALOG.values():
        names.update(group_tools)
    return names


def main() -> int:
    expected = _expected_tool_names()
    found = _catalog_tool_names()
    missing = sorted(expected - found)
    extra = sorted(found - expected - {"ua_check_setup"})

    if missing or extra:
        if missing:
            print("Missing tools:", missing)
        if extra:
            print("Unexpected tools:", extra)
        return 1

    print("Parity check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
