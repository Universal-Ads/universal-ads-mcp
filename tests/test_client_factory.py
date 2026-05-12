"""Client factory behavior tests."""

from __future__ import annotations

import pytest

import ua_mcp.client_factory as client_factory
from ua_mcp import __version__
from ua_mcp.config import UAConfig


def test_build_client_sets_mcp_headers(monkeypatch) -> None:
    captured_kwargs: dict = {}

    class FakeClient:
        def __init__(self, **kwargs):
            captured_kwargs.update(kwargs)

    monkeypatch.setattr(client_factory, "UniversalAdsClient", FakeClient)

    config = UAConfig(
        api_key="test-api-key",
        private_key_pem="test-private-key",
        base_url="https://api.universalads.com/v1",
    )
    client_factory._build_client(config)

    assert captured_kwargs["headers"]["x-ua-client"] == "mcp"
    assert captured_kwargs["headers"]["x-ua-mcp-version"] == __version__


def test_validate_sdk_version_accepts_required_version(monkeypatch) -> None:
    monkeypatch.setattr(client_factory, "_get_installed_sdk_version", lambda: "2.0.0")
    client_factory.validate_sdk_version()


def test_validate_sdk_version_rejects_mismatch(monkeypatch) -> None:
    monkeypatch.setattr(client_factory, "_get_installed_sdk_version", lambda: "1.9.9")
    with pytest.raises(RuntimeError, match="requires universal-ads-sdk==2.0.0"):
        client_factory.validate_sdk_version()
