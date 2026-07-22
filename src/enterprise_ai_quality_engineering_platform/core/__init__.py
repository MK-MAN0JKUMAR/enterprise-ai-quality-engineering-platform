"""
Core runtime components for the Enterprise AI Quality Engineering Platform.

This package contains platform metadata, runtime information,
and shared core functionality that is independent of any
AI provider or infrastructure implementation.
"""

from .metadata import (
    PACKAGE_NAME,
    PROJECT_NAME,
    PYTHON_MIN_VERSION,
    VERSION,
)

__all__ = [
    "PACKAGE_NAME",
    "PROJECT_NAME",
    "VERSION",
    "PYTHON_MIN_VERSION",
]
