"""
Tests for URL validation utilities.
"""

import pytest

from enterprise_ai_testing_platform.validation.urls import (
    validate_http_url,
    validate_https_url,
)


def test_validate_http_url() -> None:
    """Validate HTTP URL."""

    assert validate_http_url("https://example.com") == "https://example.com"


def test_validate_http_url_invalid() -> None:
    """Reject invalid URL."""

    with pytest.raises(ValueError):
        validate_http_url("invalid")


def test_validate_https_url() -> None:
    """Validate HTTPS URL."""

    assert validate_https_url("https://example.com") == "https://example.com"


def test_validate_https_url_invalid() -> None:
    """Reject non-HTTPS URL."""

    with pytest.raises(ValueError):
        validate_https_url("http://example.com")
