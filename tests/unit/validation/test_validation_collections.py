"""
Tests for collection validation utilities.
"""

import pytest

from enterprise_ai_testing_platform.validation.collections import (
    validate_length,
    validate_not_empty,
    validate_unique,
)


def test_validate_not_empty() -> None:
    """Validate non-empty collection."""

    values = [1, 2, 3]

    assert validate_not_empty(values) == values


def test_validate_not_empty_invalid() -> None:
    """Reject empty collection."""

    with pytest.raises(ValueError):
        validate_not_empty([])


def test_validate_length() -> None:
    """Validate collection length."""

    values = [1, 2, 3]

    assert validate_length(values, minimum=2) == values


def test_validate_unique() -> None:
    """Validate unique collection."""

    values = [1, 2, 3]

    assert validate_unique(values) == values


def test_validate_unique_invalid() -> None:
    """Reject duplicate values."""

    with pytest.raises(ValueError):
        validate_unique([1, 2, 2])
