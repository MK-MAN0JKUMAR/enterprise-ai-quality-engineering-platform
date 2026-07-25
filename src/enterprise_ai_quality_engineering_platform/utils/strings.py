"""
String utility functions.
"""

from __future__ import annotations

import re

_SLUG_PATTERN = re.compile(r"[^a-z0-9]+")


def normalize_whitespace(value: str) -> str:
    """
    Normalize whitespace within a string.

    Consecutive whitespace characters are replaced with a single space and
    leading/trailing whitespace is removed.

    Args:
        value:
            Input string.

    Returns:
        Normalized string.
    """

    return " ".join(value.split())


def slugify(value: str) -> str:
    """
    Convert a string into a URL-friendly slug.

    The resulting slug:

    - uses lowercase characters
    - replaces non-alphanumeric characters with hyphens
    - removes duplicate hyphens
    - removes leading and trailing hyphens

    Args:
        value:
            Input string.

    Returns:
        URL-friendly slug.
    """

    slug = value.strip().lower()
    slug = _SLUG_PATTERN.sub("-", slug)

    return slug.strip("-")
