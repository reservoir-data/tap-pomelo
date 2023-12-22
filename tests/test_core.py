"""Tests standard tap features using the built-in SDK tests library."""

from __future__ import annotations

from typing import Any

from singer_sdk.testing import SuiteConfig, get_tap_test_class

from tap_pomelo.tap import TapPomelo

SAMPLE_CONFIG: dict[str, Any] = {}

TestTapPomelo = get_tap_test_class(
    TapPomelo,
    config=SAMPLE_CONFIG,
    suite_config=SuiteConfig(ignore_no_records_for_streams=["companies"]),
)
