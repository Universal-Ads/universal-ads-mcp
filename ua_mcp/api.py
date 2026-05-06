"""Thin wrappers around UniversalAdsClient read-only methods."""

from __future__ import annotations

from typing import Any

from .client_factory import get_client
from .errors import raise_user_error


def call(method_name: str, **kwargs: Any) -> dict[str, Any]:
    """Invoke a read method and normalize failures."""
    client = get_client()
    method = getattr(client, method_name)
    try:
        result = method(**kwargs)
    except Exception as exc:
        raise_user_error(exc)
    if isinstance(result, dict):
        return result
    return {"result": result}
