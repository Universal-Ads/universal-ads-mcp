"""Universal Ads SDK client lifecycle and startup validation."""

from __future__ import annotations

from threading import Lock

from universal_ads_sdk import UniversalAdsClient

from .config import UAConfig, resolve_config
from .errors import raise_user_error

_client_lock = Lock()
_client: UniversalAdsClient | None = None
_config: UAConfig | None = None


def _build_client(config: UAConfig) -> UniversalAdsClient:
    return UniversalAdsClient(
        api_key=config.api_key,
        private_key_pem=config.private_key_pem,
        base_url=config.base_url,
    )


def get_config() -> UAConfig:
    """Load config once and reuse it."""
    global _config
    if _config is None:
        _config = resolve_config()
    return _config


def get_client() -> UniversalAdsClient:
    """Return a singleton SDK client for all tools."""
    global _client
    if _client is not None:
        return _client

    with _client_lock:
        if _client is None:
            try:
                _client = _build_client(get_config())
            except Exception as exc:
                raise_user_error(exc)
        return _client


def validate_startup_credentials() -> None:
    """Fail fast on invalid local env configuration."""
    # This validates env presence and PEM/key parsing via client construction.
    get_client()


def _reset_cache_for_tests() -> None:
    """Clear module-level cache (test-only helper)."""
    global _client, _config
    _client = None
    _config = None
