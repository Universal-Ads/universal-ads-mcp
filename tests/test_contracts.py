"""Contract assertions for annotations and structured output."""

from __future__ import annotations

from ua_mcp.tools import register_tools


def test_tools_are_structured_and_readonly(fake_registry) -> None:
    register_tools(fake_registry)
    for name, details in fake_registry.tools.items():
        kwargs = details["kwargs"]
        assert kwargs.get("structured_output") is True
        annotations = kwargs.get("annotations")
        assert annotations is not None
        assert getattr(annotations, "readOnlyHint", False) is True
        assert getattr(annotations, "destructiveHint", True) is False
        if name != "ua_get_scheduled_report":
            assert getattr(annotations, "idempotentHint", False) is True
