"""Reporting endpoint tools."""

from __future__ import annotations

from typing import Any

from .. import api
from ..tool_contract import READ_ONLY_TOOL, normalize_limit, tool_response


def register_report_tools(mcp: object) -> None:
    @mcp.tool(annotations=READ_ONLY_TOOL, structured_output=True)
    def ua_get_campaign_report(
        adaccount_id: str,
        start_date: str | None = None,
        end_date: str | None = None,
        campaign_ids: list[str] | None = None,
        date_aggregation: str | None = None,
        attribution_window: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> dict[str, Any]:
        """Fetch a campaign-level performance report.

        Limit 1-20 per request (default 10); paginate via offset.

        Args:
            start_date: Start of the reporting window. ISO 8601 datetime
                including the time component, e.g. "2026-05-12T00:00:00".
                Date-only values are rejected.
            end_date: End of the reporting window. Same format as start_date.
            date_aggregation: Time bucketing for the report. Allowed values:
                "HOUR", "DAY", "LIFETIME", "TOTAL" — note these are UPPERCASE.
                DAY/HOUR omits zero-activity buckets — zero-fill client-side
                if you need a continuous series.
            attribution_window: Conversion attribution window. Allowed values:
                "7_day", "14_day", "30_day" — lowercase. If not set, pixel-based
                conversion metrics are omitted from the response.
            campaign_ids: Filter to specific campaigns. Max 5 IDs per request.
        """
        effective_limit = normalize_limit(limit=limit, default_limit=10, max_limit=20)
        return tool_response(
            api.call(
                "get_campaign_report",
                adaccount_id=adaccount_id,
                start_date=start_date,
                end_date=end_date,
                campaign_ids=campaign_ids,
                date_aggregation=date_aggregation,
                attribution_window=attribution_window,
                limit=effective_limit,
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
        date_aggregation: str | None = None,
        attribution_window: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> dict[str, Any]:
        """Fetch an ad-set-level performance report.

        Limit 1-20 per request (default 10); paginate via offset.

        Args:
            start_date: Start of the reporting window. ISO 8601 datetime
                including the time component, e.g. "2026-05-12T00:00:00".
                Date-only values are rejected.
            end_date: End of the reporting window. Same format as start_date.
            date_aggregation: Time bucketing for the report. Allowed values:
                "HOUR", "DAY", "LIFETIME", "TOTAL" — note these are UPPERCASE.
                DAY/HOUR omits zero-activity buckets — zero-fill client-side
                if you need a continuous series.
            attribution_window: Conversion attribution window. Allowed values:
                "7_day", "14_day", "30_day" — lowercase. If not set, pixel-based
                conversion metrics are omitted from the response.
            campaign_ids: Filter to specific campaigns. Max 5 IDs per request.
            adset_ids: Filter to specific ad sets. Max 5 IDs per request.
        """
        effective_limit = normalize_limit(limit=limit, default_limit=10, max_limit=20)
        return tool_response(
            api.call(
                "get_adset_report",
                adaccount_id=adaccount_id,
                start_date=start_date,
                end_date=end_date,
                campaign_ids=campaign_ids,
                adset_ids=adset_ids,
                date_aggregation=date_aggregation,
                attribution_window=attribution_window,
                limit=effective_limit,
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
        """Fetch an ad-level performance report.

        Limit 1-20 per request (default 10); paginate via offset.

        Args:
            start_date: Start of the reporting window. ISO 8601 datetime
                including the time component, e.g. "2026-05-12T00:00:00".
                Date-only values are rejected.
            end_date: End of the reporting window. Same format as start_date.
            date_aggregation: Time bucketing for the report. Allowed values:
                "HOUR", "DAY", "LIFETIME", "TOTAL" — note these are UPPERCASE.
                DAY/HOUR omits zero-activity buckets — zero-fill client-side
                if you need a continuous series.
            attribution_window: Conversion attribution window. Allowed values:
                "7_day", "14_day", "30_day" — lowercase. If not set, pixel-based
                conversion metrics are omitted from the response.
            campaign_ids: Filter to specific campaigns. Max 5 IDs per request.
            adset_ids: Filter to specific ad sets. Max 5 IDs per request.
            ad_ids: Filter to specific ads. Max 5 IDs per request.
        """
        effective_limit = normalize_limit(limit=limit, default_limit=10, max_limit=20)
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
                limit=effective_limit,
                offset=offset,
            )
        )

