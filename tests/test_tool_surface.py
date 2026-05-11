"""Tool and resource surface contract tests."""

from __future__ import annotations

from ua_mcp.resources import TOOL_CATALOG, register_resources
from ua_mcp.tools import register_tools

EXPECTED_TOOLS = {
    "ua_check_setup",
    "ua_get_organizations",
    "ua_get_adaccounts",
    "ua_get_campaigns",
    "ua_get_campaign",
    "ua_get_adsets",
    "ua_get_adset",
    "ua_get_ads",
    "ua_get_ad",
    "ua_get_creatives",
    "ua_get_creative",
    "ua_get_media",
    "ua_get_campaign_report",
    "ua_get_adset_report",
    "ua_get_ad_report",
    "ua_get_audiences",
    "ua_get_audience",
    "ua_get_pixels",
    "ua_get_pixel",
    "ua_get_pixel_events",
}


def test_tool_surface(fake_registry) -> None:
    register_tools(fake_registry)
    assert set(fake_registry.tools.keys()) == EXPECTED_TOOLS


def test_no_mutation_tools(fake_registry) -> None:
    register_tools(fake_registry)
    names = set(fake_registry.tools.keys())
    forbidden = {"create", "update", "delete", "upload", "verify", "schedule"}
    assert not any(any(token in name for token in forbidden) for name in names)


def test_catalog_matches_tools(fake_registry) -> None:
    register_tools(fake_registry)
    catalog_names = {name for group in TOOL_CATALOG.values() for name in group}
    assert catalog_names == EXPECTED_TOOLS


def test_resource_surface(fake_registry) -> None:
    register_resources(fake_registry)
    assert set(fake_registry.resources.keys()) == {
        "ua://setup",
        "ua://tool-catalog",
        "ua://privacy-and-safety",
    }
