"""
Provider factory.
"""

from __future__ import annotations

from enterprise_ai_testing_platform.common import ProviderType
from enterprise_ai_testing_platform.config import PlatformSettings

from .base import Provider
from .exceptions import ProviderError
from .registry import ProviderRegistry


class ProviderFactory:
    """
    Factory responsible for constructing provider instances.
    """

    def __init__(
        self,
        settings: PlatformSettings,
    ) -> None:
        self._settings = settings

    def create(
        self,
        provider: ProviderType,
    ) -> Provider:
        """
        Create a provider instance.

        Args:
            provider:
                Provider to instantiate.

        Returns:
            Provider implementation.

        Raises:
            ProviderError:
                If the provider is not supported.
        """

        if not ProviderRegistry.contains(provider):
            raise ProviderError(f"Unsupported provider: {provider}")

        return ProviderRegistry.create(
            provider,
            self._settings,
        )

    def create_default_chat_provider(self) -> Provider:
        """
        Create the configured default chat provider.
        """

        return self.create(
            self._settings.providers.default_chat_provider,
        )

    def create_default_embedding_provider(self) -> Provider:
        """
        Create the configured default embedding provider.
        """

        return self.create(
            self._settings.providers.default_embedding_provider,
        )

    def create_default_reranking_provider(self) -> Provider:
        """
        Create the configured default reranking provider.
        """

        return self.create(
            self._settings.providers.default_reranking_provider,
        )
