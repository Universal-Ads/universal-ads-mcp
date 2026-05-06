"""Reporting endpoint tools."""

from __future__ import annotations

from typing import Any

from .. import api
from ..tool_contract import READ_ONLY_TOOL, tool_response


def register_report_tools(mcp: object) -> None:
    @mcp.tool(annotations=READ_ONLY_TOOL, structured_output=True)
    def ua_get_campaign_report(
        adaccount_id: str,
        start_date: str | None = None,
        end_date: str | None = None,
        campaign_ids: list[str] | None = None,
        adset_ids: list[str] | None = None,
        ad_ids: list[str] | None = None,
        date_aggregation: str | None = None,
        attribution_window: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> dict[str, Any]:
        """Fetch campaign performance report."""
        return tool_response(
            api.call(
                "get_campaign_report",
                adaccount_id=adaccount_id,
                start_date=start_date,
                end_date=end_date,
                campaign_ids=campaign_ids,
                adset_ids=adset_ids,
                ad_ids=ad_ids,
                date_aggregation=date_aggregation,
                attribution_window=attribution_window,
                limit=limit,
                offset=offset,
            )
        )

    @mcp.tool(annotations=READ_ONLY_TOOL, structured_output=True)
    def ua_get_adset_report(
        adaccount_id: str,
        start_date: str | None = None,
        end_date: str | None = None,
        campaign_ids: list[str] | None = None,
        adset_ids: list[str] | None = None,
        ad_ids: list[str] | None = None,
        date_aggregation: str | None = None,
        attribution_window: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> dict[str, Any]:
        """Fetch ad set performance report."""
        return tool_response(
            api.call(
                "get_adset_report",
                adaccount_id=adaccount_id,
                start_date=start_date,
                end_date=end_date,
                campaign_ids=campaign_ids,
                adset_ids=adset_ids,
                ad_ids=ad_ids,
                date_aggregation=date_aggregation,
                attribution_window=attribution_window,
                limit=limit,
                offset=offset,
            )
        )

    @mcp.tool(annotations=READ_ONLY_TOOL, structured_output=True)
    def ua_get_ad_report(
        adaccount_id: str,
        start_date: str | None = None,
        end_date: str | None = None,
        campaign_ids: list[str] | None = None,
        adset_ids: list[str] | None = None,
        ad_ids: list[str] | None = None,
        date_aggregation: str | None = None,
        attribution_window: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> dict[str, Any]:
        """Fetch ad performance report."""
        return tool_response(
            api.call(
                "get_ad_report",
                adaccount_id=adaccount_id,
                start_date=start_date,
                end_date=end_date,
                campaign_ids=campaign_ids,
                adset_ids=adset_ids,
                ad_ids=ad_ids,
                date_aggregation=date_aggregation,
                attribution_window=attribution_window,
                limit=limit,
                offset=offset,
            )
        )

    @mcp.tool(annotations=READ_ONLY_TOOL, structured_output=True)
    def ua_get_scheduled_report(
        scheduled_report_id: str,
        include_result_url: bool = False,
    ) -> dict[str, Any]:
        """Fetch scheduled report status/output metadata."""
        return tool_response(
            api.call("get_scheduled_report", scheduled_report_id=scheduled_report_id),
            include_result_url=include_result_url,
        )
