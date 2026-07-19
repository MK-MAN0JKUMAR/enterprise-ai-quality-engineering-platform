"""
Tests for environment definitions.
"""

from enterprise_ai_testing_platform.config import Environment


def test_environment_values() -> None:
    """Verify environment enum values."""

    assert Environment.DEVELOPMENT == "development"
    assert Environment.TESTING == "testing"
    assert Environment.STAGING == "staging"
    assert Environment.PRODUCTION == "production"
