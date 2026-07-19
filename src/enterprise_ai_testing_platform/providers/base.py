"""
Provider protocol.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from .types import ProviderMetadata


class Provider(ABC):
    """
    Base class implemented by every provider.
    """

    @property
    @abstractmethod
    def metadata(self) -> ProviderMetadata:
        """
        Return provider metadata.
        """

    @abstractmethod
    def initialize(self) -> None:
        """
        Initialize the provider.
        """

    @abstractmethod
    def shutdown(self) -> None:
        """
        Shutdown the provider.
        """

    @property
    @abstractmethod
    def is_initialized(self) -> bool:
        """
        Whether the provider has been initialized.
        """
