"""Test fixtures for MCP registry capture."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable
import pytest


@dataclass
class FakeRegistry:
    tools: dict[str, dict[str, Any]] = field(default_factory=dict)
    resources: dict[str, dict[str, Any]] = field(default_factory=dict)

    def tool(self, **kwargs: Any) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
        def decorator(fn: Callable[..., Any]) -> Callable[..., Any]:
            self.tools[fn.__name__] = {"fn": fn, "kwargs": kwargs}
            return fn

        return decorator

    def resource(
        self, uri: str, **kwargs: Any
    ) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
        def decorator(fn: Callable[..., Any]) -> Callable[..., Any]:
            self.resources[uri] = {"fn": fn, "kwargs": kwargs}
            return fn

        return decorator


@pytest.fixture
def fake_registry() -> FakeRegistry:
    return FakeRegistry()
