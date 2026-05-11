"""Me endpoint tools."""

from __future__ import annotations

from typing import Any

from .. import api
from ..tool_contract import READ_ONLY_TOOL, normalize_limit, tool_response


def register_me_tools(mcp: object) -> None:
    @mcp.tool(annotations=READ_ONLY_TOOL, structured_output=True)
    def ua_get_organizations(limit: int | None = None, offset: int | None = None) -> dict[str, Any]:
        """List organizations visible to this credential. limit: 1-100 (SDK docs; default 10)."""
        effective_limit = normalize_limit(limit=limit, default_limit=10, max_limit=100)
        return tool_response(
            api.call("get_organizations", limit=effective_limit, offset=offset)
        )

    @mcp.tool(annotations=READ_ONLY_TOOL, structured_output=True)
    def ua_get_adaccounts(
        limit: int | None = None,
        offset: int | None = None,
        organization_ids: list[str] | None = None,
        authorization_statuses: list[str] | None = None,
    ) -> dict[str, Any]:
        """List ad accounts visible to this credential. limit: 1-100 (SDK docs; default 10)."""
        effective_limit = normalize_limit(limit=limit, default_limit=10, max_limit=100)
        return tool_response(
            api.call(
                "get_adaccounts",
                limit=effective_limit,
                offset=offset,
                organization_ids=organization_ids,
                authorization_statuses=authorization_statuses,
            )
        )
