"""Shared MCP tool annotations and response envelopes."""

from __future__ import annotations

from typing import Any

from mcp.types import ToolAnnotations

from .privacy import redact_response

READ_ONLY_TOOL = ToolAnnotations(
    readOnlyHint=True,
    destructiveHint=False,
    idempotentHint=True,
    openWorldHint=True,
)


def tool_response(
    data: Any,
    *,
    warnings: list[str] | None = None,
    include_result_url: bool = False,
) -> dict[str, Any]:
    """Return a stable structured payload for all tools."""
    return {
        "data": redact_response(data, include_result_url=include_result_url),
        "warnings": warnings or [],
    }


def normalize_limit(*, limit: int | None, default_limit: int, max_limit: int) -> int:
    """Return a bounded limit with an MCP-side default."""
    effective_limit = default_limit if limit is None else limit
    if effective_limit < 1:
        raise ValueError("limit must be >= 1")
    if effective_limit > max_limit:
        raise ValueError(f"limit must be <= {max_limit}")
    return effective_limit
