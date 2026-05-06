"""Response redaction utilities."""

from __future__ import annotations

from typing import Any
from urllib.parse import urlsplit, urlunsplit

SENSITIVE_KEYS = {"access_token", "script", "authorization", "signature", "private_key"}
URL_KEYS = {"url", "result_url", "download_url"}


def _strip_query(value: str) -> str:
    parsed = urlsplit(value)
    if not parsed.scheme:
        return value
    return urlunsplit((parsed.scheme, parsed.netloc, parsed.path, "", parsed.fragment))


def redact_response(value: Any, *, include_result_url: bool = False) -> Any:
    """Recursively redact sensitive values from tool payloads."""
    if isinstance(value, dict):
        result: dict[str, Any] = {}
        for key, item in value.items():
            lowered = key.lower()
            if lowered in SENSITIVE_KEYS:
                result[key] = "[REDACTED]"
                continue
            if lowered == "result_url" and not include_result_url:
                result[key] = "[REDACTED]"
                continue
            if lowered in URL_KEYS and isinstance(item, str):
                result[key] = _strip_query(item)
                continue
            result[key] = redact_response(item, include_result_url=include_result_url)
        return result
    if isinstance(value, list):
        return [redact_response(item, include_result_url=include_result_url) for item in value]
    return value
