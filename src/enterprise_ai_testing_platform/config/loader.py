"""
Configuration loader.
"""

from __future__ import annotations

from functools import cache

from .platform import PlatformSettings


@cache
def get_settings() -> PlatformSettings:
    """Return the singleton platform settings."""

    return PlatformSettings()
