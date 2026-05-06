"""Parity script smoke test."""

from __future__ import annotations

from scripts.check_parity import main


def test_parity_script_passes() -> None:
    assert main() == 0
