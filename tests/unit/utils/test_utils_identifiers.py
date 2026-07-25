"""
Tests for identifier utilities.
"""

from uuid import UUID

from enterprise_ai_quality_engineering_platform.utils import generate_uuid


def test_generate_uuid_returns_valid_uuid() -> None:
    """Verify generate_uuid returns a valid UUID string."""

    value = generate_uuid()

    parsed = UUID(value)

    assert str(parsed) == value
