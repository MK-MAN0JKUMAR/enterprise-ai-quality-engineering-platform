"""
Identifier utility functions.
"""

from __future__ import annotations

from uuid import uuid4


def generate_uuid() -> str:
    """
    Generate a random UUID version 4.

    Returns:
        UUID string.
    """

    return str(uuid4())
