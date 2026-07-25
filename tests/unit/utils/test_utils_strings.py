"""
Tests for string utilities.
"""

from enterprise_ai_quality_engineering_platform.utils import (
    normalize_whitespace,
    slugify,
)


def test_normalize_whitespace() -> None:
    """Verify whitespace normalization."""

    value = "  Enterprise     AI     Quality   Engineering   Platform   "

    assert normalize_whitespace(value) == "Enterprise AI Quality Engineering Platform"


def test_slugify() -> None:
    """Verify slug generation."""

    value = "Enterprise AI Quality Engineering Platform"

    assert slugify(value) == "enterprise-ai-quality-engineering-platform"
