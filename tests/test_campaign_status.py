"""Tests for ua_get_campaigns status list contract and forwarding."""

from __future__ import annotations

from typing import get_type_hints

from ua_mcp.tools import register_tools


def _get_campaigns_tool(fake_registry):
    register_tools(fake_registry)
    return fake_registry.tools["ua_get_campaigns"]["fn"]


def test_ua_get_campaigns_status_annotation_is_list(fake_registry) -> None:
    fn = _get_campaigns_tool(fake_registry)
    hints = get_type_hints(fn)
    assert hints["status"] == list[str] | None


def test_ua_get_campaigns_forwards_status_list(fake_registry, monkeypatch) -> None:
    captured: dict = {}

    def fake_call(method_name: str, **kwargs):
        captured["method_name"] = method_name
        captured["kwargs"] = kwargs
        return {"data": []}

    monkeypatch.setattr("ua_mcp.tools.campaign.api.call", fake_call)

    fn = _get_campaigns_tool(fake_registry)
    fn(adaccount_id="acc_1", status=["active", "paused"])

    assert captured["method_name"] == "get_campaigns"
    assert captured["kwargs"]["status"] == ["active", "paused"]
    assert captured["kwargs"]["adaccount_id"] == "acc_1"
    assert captured["kwargs"]["limit"] == 10


def test_ua_get_campaigns_forwards_status_none(fake_registry, monkeypatch) -> None:
    captured: dict = {}

    def fake_call(method_name: str, **kwargs):
        captured["kwargs"] = kwargs
        return {"data": []}

    monkeypatch.setattr("ua_mcp.tools.campaign.api.call", fake_call)

    fn = _get_campaigns_tool(fake_registry)
    fn(adaccount_id="acc_1")

    assert captured["kwargs"]["status"] is None


def test_ua_get_campaigns_forwards_status_empty_list(fake_registry, monkeypatch) -> None:
    captured: dict = {}

    def fake_call(method_name: str, **kwargs):
        captured["kwargs"] = kwargs
        return {"data": []}

    monkeypatch.setattr("ua_mcp.tools.campaign.api.call", fake_call)

    fn = _get_campaigns_tool(fake_registry)
    fn(adaccount_id="acc_1", status=[])

    assert captured["kwargs"]["status"] == []


def test_ua_get_campaigns_docstring_documents_multi_status(fake_registry) -> None:
    fn = _get_campaigns_tool(fake_registry)
    assert fn.__doc__ is not None
    assert "status" in fn.__doc__
    assert "active" in fn.__doc__
    assert "paused" in fn.__doc__
