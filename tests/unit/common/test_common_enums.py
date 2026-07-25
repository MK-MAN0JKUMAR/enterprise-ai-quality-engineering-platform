"""
Tests for shared enums.
"""

from enterprise_ai_quality_engineering_platform.common.enums import (
    Environment,
    LogLevel,
)


def test_environment_values() -> None:
    """Verify environment enum values."""

    assert Environment.DEVELOPMENT == "development"
    assert Environment.TESTING == "testing"
    assert Environment.STAGING == "staging"
    assert Environment.PRODUCTION == "production"


def test_log_level_values() -> None:
    """Verify log level enum values."""

    assert LogLevel.DEBUG == "DEBUG"
    assert LogLevel.INFO == "INFO"
    assert LogLevel.WARNING == "WARNING"
    assert LogLevel.ERROR == "ERROR"
    assert LogLevel.CRITICAL == "CRITICAL"
