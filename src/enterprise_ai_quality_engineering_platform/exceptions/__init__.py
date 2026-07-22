"""
Platform exception hierarchy.
"""

from .base import PlatformError, PlatformRuntimeError
from .configuration import ConfigurationError
from .plugin import PluginError
from .provider import ProviderError
from .validation import ValidationError

__all__ = [
    "ConfigurationError",
    "PlatformError",
    "PlatformRuntimeError",
    "PluginError",
    "ProviderError",
    "ValidationError",
]
