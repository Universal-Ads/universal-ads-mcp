"""Credential and config behavior tests."""

from __future__ import annotations

import pytest

from ua_mcp.client_factory import _reset_cache_for_tests, get_config
from ua_mcp.config import normalize_private_key


@pytest.fixture(autouse=True)
def reset_cache() -> None:
    _reset_cache_for_tests()


def test_missing_api_key_raises(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("UNIVERSAL_ADS_API_KEY", raising=False)
    monkeypatch.delenv("UNIVERSAL_ADS_PRIVATE_KEY", raising=False)
    with pytest.raises(ValueError, match="UNIVERSAL_ADS_API_KEY"):
        get_config()


def test_missing_private_key_raises(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("UNIVERSAL_ADS_API_KEY", "abc123")
    monkeypatch.delenv("UNIVERSAL_ADS_PRIVATE_KEY", raising=False)
    with pytest.raises(ValueError, match="UNIVERSAL_ADS_PRIVATE_KEY"):
        get_config()


def test_base_url_defaults(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("UNIVERSAL_ADS_API_KEY", "abc123")
    monkeypatch.setenv(
        "UNIVERSAL_ADS_PRIVATE_KEY",
        "-----BEGIN EC PRIVATE KEY-----\ninvalid\n-----END EC PRIVATE KEY-----",
    )
    monkeypatch.delenv("UNIVERSAL_ADS_BASE_URL", raising=False)
    config = get_config()
    assert config.base_url == "https://api.universalads.com/v1"


def test_normalize_private_key_escaped_newlines() -> None:
    raw = "-----BEGIN EC PRIVATE KEY-----\\nline2\\n-----END EC PRIVATE KEY-----"
    normalized = normalize_private_key(raw)
    assert "\\n" not in normalized
    assert "\nline2\n" in normalized
