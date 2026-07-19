"""
Shared protocols.
"""

from typing import Protocol


class SupportsName(Protocol):
    """
    Protocol for objects exposing a name.
    """

    @property
    def name(self) -> str:
        """
        Object name.
        """
        ...
