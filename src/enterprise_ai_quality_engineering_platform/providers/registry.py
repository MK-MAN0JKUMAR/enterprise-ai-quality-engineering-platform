"""
Provider registry.

Maintains the mapping between provider types and their runtime
implementations. The registry is intentionally static for now to
provide a single source of truth for provider registration while
keeping provider discovery simple and explicit.
"""

from __future__ import annotations

from collections.abc import Callable

from enterprise_ai_quality_engineering_platform.common import ProviderType
from enterprise_ai_quality_engineering_platform.config import PlatformSettings

from .base import Provider
from .gemini import GeminiProvider
from .groq import GroqProvider
from .lmstudio import LMStudioProvider
from .ollama import OllamaProvider

type ProviderConstructor = Callable[
    [PlatformSettings],
    Provider,
]


class ProviderRegistry:
    """
    Registry of supported runtime providers.
    """

    _REGISTRY: dict[ProviderType, ProviderConstructor] = {
        ProviderType.GROQ: lambda settings: GroqProvider(
            settings.providers.groq,
        ),
        ProviderType.OLLAMA: lambda settings: OllamaProvider(
            settings.providers.ollama,
        ),
        ProviderType.LMSTUDIO: lambda settings: LMStudioProvider(
            settings.providers.lmstudio,
        ),
        ProviderType.GEMINI: lambda settings: GeminiProvider(
            settings.providers.gemini,
        ),
    }

    @classmethod
    def contains(
        cls,
        provider: ProviderType,
    ) -> bool:
        """
        Return whether the provider is registered.
        """

        return provider in cls._REGISTRY

    @classmethod
    def create(
        cls,
        provider: ProviderType,
        settings: PlatformSettings,
    ) -> Provider:
        """
        Create a provider instance.

        Raises
        ------
        KeyError
            If the provider has not been registered.
        """

        constructor = cls._REGISTRY[provider]

        return constructor(settings)

    @classmethod
    def registered_providers(
        cls,
    ) -> tuple[ProviderType, ...]:
        """
        Return all registered providers.
        """

        return tuple(cls._REGISTRY.keys())
