"""
Hashing utility functions.
"""

from __future__ import annotations

import hashlib


def md5_hash(value: str) -> str:
    """
    Generate an MD5 hash for the provided string.

    Args:
        value:
            Input string.

    Returns:
        Hexadecimal MD5 hash.
    """

    return hashlib.md5(value.encode("utf-8"), usedforsecurity=False).hexdigest()


def sha256_hash(value: str) -> str:
    """
    Generate a SHA-256 hash for the provided string.

    Args:
        value:
            Input string.

    Returns:
        Hexadecimal SHA-256 hash.
    """

    return hashlib.sha256(value.encode("utf-8")).hexdigest()
