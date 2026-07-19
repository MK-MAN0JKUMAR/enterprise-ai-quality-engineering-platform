"""
Ollama provider implementation.
"""

from __future__ import annotations

from enterprise_ai_testing_platform.providers.base import Provider
from enterprise_ai_testing_platform.providers.types import ProviderMetadata

from .constants import (
    PROVIDER_NAME,
    PROVIDER_VENDOR,
    PROVIDER_VERSION,
    SUPPORTED_CAPABILITIES,
)


class OllamaProvider(Provider):
    """
    Ollama provider implementation.

    This class currently implements only the provider lifecycle.
    AI inference capabilities will be added in future feature branches.
    """

    def __init__(self) -> None:
        self._initialized = False

        self._metadata = ProviderMetadata(
            name=PROVIDER_NAME,
            vendor=PROVIDER_VENDOR,
            version=PROVIDER_VERSION,
            capabilities=SUPPORTED_CAPABILITIES,
        )

    @property
    def metadata(self) -> ProviderMetadata:
        """
        Return provider metadata.
        """
        return self._metadata

    def initialize(self) -> None:
        """
        Initialize the provider.
        """
        self._initialized = True

    def shutdown(self) -> None:
        """
        Shutdown the provider.
        """
        self._initialized = False

    @property
    def is_initialized(self) -> bool:
        """
        Whether the provider has been initialized.
        """
        return self._initialized
