"""
Tests for text validation utilities.
"""

import pytest

from enterprise_ai_quality_engineering_platform.validation.text import (
    validate_identifier,
    validate_max_length,
    validate_min_length,
    validate_not_blank,
)


def test_validate_not_blank() -> None:
    """Validate non-blank string."""

    assert validate_not_blank("hello") == "hello"


def test_validate_not_blank_invalid() -> None:
    """Reject blank string."""

    with pytest.raises(ValueError):
        validate_not_blank("   ")


def test_validate_min_length() -> None:
    """Validate minimum length."""

    assert validate_min_length("hello", 3) == "hello"


def test_validate_max_length() -> None:
    """Validate maximum length."""

    assert validate_max_length("hello", 10) == "hello"


def test_validate_identifier() -> None:
    """Validate identifier."""

    assert validate_identifier("project_name") == "project_name"
