"""
Tests for datetime utilities.
"""

from datetime import UTC, datetime

from enterprise_ai_testing_platform.utils import (
    current_utc_datetime,
    current_utc_timestamp,
)


def test_current_utc_datetime_returns_datetime() -> None:
    """Verify current_utc_datetime returns a UTC-aware datetime."""

    value = current_utc_datetime()

    assert isinstance(value, datetime)
    assert value.tzinfo is UTC


def test_current_utc_timestamp_returns_iso8601_string() -> None:
    """Verify current_utc_timestamp returns a valid ISO 8601 timestamp."""

    timestamp = current_utc_timestamp()

    parsed = datetime.fromisoformat(timestamp)

    assert parsed.tzinfo is UTC
