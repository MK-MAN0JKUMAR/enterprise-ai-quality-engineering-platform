"""
Shared utility functions for the Enterprise AI Testing Platform.

This package provides reusable, framework-agnostic helper functions that are
used throughout the platform. Utilities in this package should remain free of
business logic and external service dependencies.
"""

from .datetime import current_utc_datetime, current_utc_timestamp
from .filesystem import ensure_directory
from .hashing import md5_hash, sha256_hash
from .identifiers import generate_uuid
from .json import read_json_file, write_json_file
from .strings import normalize_whitespace, slugify

__all__ = [
    "current_utc_datetime",
    "current_utc_timestamp",
    "ensure_directory",
    "generate_uuid",
    "md5_hash",
    "normalize_whitespace",
    "read_json_file",
    "sha256_hash",
    "slugify",
    "write_json_file",
]
