"""
Tests for string utilities.
"""

from enterprise_ai_testing_platform.utils import (
    normalize_whitespace,
    slugify,
)


def test_normalize_whitespace() -> None:
    """Verify whitespace normalization."""

    value = "  Enterprise     AI     Testing   Platform   "

    assert normalize_whitespace(value) == "Enterprise AI Testing Platform"


def test_slugify() -> None:
    """Verify slug generation."""

    value = "Enterprise AI Testing Platform"

    assert slugify(value) == "enterprise-ai-testing-platform"
