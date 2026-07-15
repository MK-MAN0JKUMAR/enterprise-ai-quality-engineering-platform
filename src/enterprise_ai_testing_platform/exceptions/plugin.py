"""
Plugin-related exceptions.
"""

from __future__ import annotations

from .base import PlatformError


class PluginError(PlatformError):
    """Base exception for plugin implementations."""
