"""
Date and time utility functions.

All date and time values are generated in Coordinated Universal Time (UTC) to
ensure consistent behavior across environments and deployments.
"""

from __future__ import annotations

from datetime import UTC, datetime


def current_utc_datetime() -> datetime:
    """
    Return the current UTC datetime.

    Returns:
        Current timezone-aware UTC datetime.
    """

    return datetime.now(tz=UTC)


def current_utc_timestamp() -> str:
    """
    Return the current UTC timestamp in ISO 8601 format.

    Returns:
        ISO 8601 formatted UTC timestamp.
    """

    return current_utc_datetime().isoformat(timespec="seconds")
