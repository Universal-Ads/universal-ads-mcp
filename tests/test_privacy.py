"""Redaction behavior tests."""

from __future__ import annotations

from ua_mcp.tool_contract import tool_response


def test_redacts_sensitive_keys() -> None:
    payload = {
        "access_token": "token",
        "script": "<script>",
        "url": "https://example.com/path?sig=abc",
    }
    result = tool_response(payload)
    assert result["data"]["access_token"] == "[REDACTED]"
    assert result["data"]["script"] == "[REDACTED]"
    assert result["data"]["url"] == "https://example.com/path"


def test_result_url_hidden_by_default() -> None:
    payload = {"result_url": "https://example.com/report.csv?signature=abc"}
    result = tool_response(payload)
    assert result["data"]["result_url"] == "[REDACTED]"


def test_result_url_available_when_requested() -> None:
    payload = {"result_url": "https://example.com/report.csv?signature=abc"}
    result = tool_response(payload, include_result_url=True)
    assert result["data"]["result_url"] == "https://example.com/report.csv"
