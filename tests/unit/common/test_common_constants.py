"""
Tests for shared constants.
"""

from enterprise_ai_quality_engineering_platform.common.constants import (
    DEFAULT_ENCODING,
    DEFAULT_TIMEOUT_SECONDS,
)


def test_default_encoding() -> None:
    """Verify default encoding."""

    assert DEFAULT_ENCODING == "utf-8"


def test_default_timeout() -> None:
    """Verify default timeout."""

    assert DEFAULT_TIMEOUT_SECONDS == 30
