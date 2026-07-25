"""
Tests for logging formatter.
"""

from enterprise_ai_quality_engineering_platform.logging.formatter import PlatformFormatter


def test_platform_formatter_can_be_created() -> None:
    """Verify formatter initialization."""

    formatter = PlatformFormatter()

    assert formatter is not None
