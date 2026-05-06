"""Environment-backed configuration for the Universal Ads MCP server."""

from __future__ import annotations

from dataclasses import dataclass
import os

DEFAULT_BASE_URL = "https://api.universalads.com/v1"


@dataclass(frozen=True)
class UAConfig:
    """Normalized runtime config for SDK client creation."""

    api_key: str
    private_key_pem: str
    base_url: str


def normalize_private_key(raw_private_key: str) -> str:
    """Normalize env-provided PEM text for SDK consumption."""
    private_key_pem = raw_private_key.strip()
    # Support .env/JSON escaped newlines.
    if "\\n" in private_key_pem:
        private_key_pem = private_key_pem.replace("\\r\\n", "\n").replace("\\n", "\n")
    return private_key_pem


def resolve_config() -> UAConfig:
    """Load and validate required environment variables."""
    api_key = os.getenv("UNIVERSAL_ADS_API_KEY", "").strip()
    private_key_pem = normalize_private_key(os.getenv("UNIVERSAL_ADS_PRIVATE_KEY", ""))
    base_url = os.getenv("UNIVERSAL_ADS_BASE_URL", DEFAULT_BASE_URL).strip() or DEFAULT_BASE_URL

    if not api_key:
        raise ValueError("Missing required env var UNIVERSAL_ADS_API_KEY")
    if not private_key_pem:
        raise ValueError("Missing required env var UNIVERSAL_ADS_PRIVATE_KEY")

    return UAConfig(api_key=api_key, private_key_pem=private_key_pem, base_url=base_url)


def masked_api_key(api_key: str) -> str:
    """Return only the key tail for safe diagnostics."""
    if len(api_key) <= 6:
        return "***"
    return f"***{api_key[-6:]}"
