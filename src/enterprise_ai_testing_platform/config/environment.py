"""
Application environment definitions.
"""

from __future__ import annotations

from enum import StrEnum


class Environment(StrEnum):
    """Supported application environments."""

    DEVELOPMENT = "development"
    TESTING = "testing"
    STAGING = "staging"
    PRODUCTION = "production"
