"""Limit guardrail tests for MCP tool wrappers."""

from __future__ import annotations

import pytest

from ua_mcp.tools import register_tools


@pytest.mark.parametrize(
    ("tool_name", "kwargs", "expected_error"),
    [
        ("ua_get_campaigns", {"limit": 101}, "limit must be <= 100"),
        ("ua_get_adsets", {"limit": 101}, "limit must be <= 100"),
        ("ua_get_ads", {"limit": 101}, "limit must be <= 100"),
        ("ua_get_creatives", {"limit": 101}, "limit must be <= 100"),
        ("ua_get_pixels", {"limit": 101}, "limit must be <= 100"),
        ("ua_get_pixel_events", {"pixel_id": "pix_1", "limit": 101}, "limit must be <= 100"),
        ("ua_get_audiences", {"adaccount_id": "acc_1", "limit": 101}, "limit must be <= 100"),
        ("ua_get_organizations", {"limit": 101}, "limit must be <= 100"),
        ("ua_get_adaccounts", {"limit": 101}, "limit must be <= 100"),
        ("ua_get_campaign_report", {"adaccount_id": "acc_1", "limit": 21}, "limit must be <= 20"),
        ("ua_get_adset_report", {"adaccount_id": "acc_1", "limit": 21}, "limit must be <= 20"),
        ("ua_get_ad_report", {"adaccount_id": "acc_1", "limit": 21}, "limit must be <= 20"),
        ("ua_get_campaigns", {"limit": 0}, "limit must be >= 1"),
    ],
)
def test_tool_limit_bounds(fake_registry, tool_name: str, kwargs: dict, expected_error: str) -> None:
    register_tools(fake_registry)
    fn = fake_registry.tools[tool_name]["fn"]
    with pytest.raises(ValueError, match=expected_error):
        fn(**kwargs)
