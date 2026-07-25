"""
Tests for service lifetime definitions.
"""

from enterprise_ai_quality_engineering_platform.services.lifetime import (
    ServiceLifetime,
)


def test_service_lifetime_values() -> None:
    """Verify service lifetime enum values."""

    assert ServiceLifetime.SINGLETON == "singleton"
    assert ServiceLifetime.TRANSIENT == "transient"
