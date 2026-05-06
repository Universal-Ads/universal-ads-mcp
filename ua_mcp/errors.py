"""Error normalization helpers for MCP tool responses."""

from __future__ import annotations

from universal_ads_sdk.common.exceptions import APIError, AuthenticationError


class UAMCPError(Exception):
    """User-safe error wrapper exposed through MCP failures."""


def api_error_message(exc: Exception) -> str:
    """Produce a concise, safe message without leaking full payloads."""
    if isinstance(exc, AuthenticationError):
        return "Authentication failed. Verify UNIVERSAL_ADS_API_KEY and UNIVERSAL_ADS_PRIVATE_KEY."

    if isinstance(exc, APIError):
        status_code = exc.status_code or "unknown"
        message = str(exc)
        response_data = exc.response_data if isinstance(exc.response_data, dict) else {}
        errors = response_data.get("errors")
        if isinstance(errors, list) and errors:
            first = errors[0]
            if isinstance(first, dict) and isinstance(first.get("message"), str):
                message = first["message"]
            elif isinstance(first, str):
                message = first
        elif isinstance(response_data.get("message"), str):
            message = response_data["message"]

        return f"Universal Ads API error (status {status_code}): {message}"

    return f"Unexpected error: {exc}"


def raise_user_error(exc: Exception) -> None:
    """Raise a safe, user-facing MCP error."""
    raise UAMCPError(api_error_message(exc)) from exc
