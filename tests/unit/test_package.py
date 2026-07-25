"""Tests for the enterprise_ai_quality_engineering_platform package."""

from __future__ import annotations

import enterprise_ai_quality_engineering_platform as platform


def test_package_version_exists() -> None:
    """Verify the package exposes a version string."""
    assert hasattr(platform, "__version__")
    assert isinstance(platform.__version__, str)
    assert platform.__version__
