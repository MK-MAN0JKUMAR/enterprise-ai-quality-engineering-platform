"""
Tests for ProviderFactory.
"""

import pytest

from enterprise_ai_testing_platform.common import ProviderType
from enterprise_ai_testing_platform.config import PlatformSettings
from enterprise_ai_testing_platform.providers import (
    GroqProvider,
    OllamaProvider,
    ProviderFactory,
)
from enterprise_ai_testing_platform.providers.exceptions import (
    ProviderError,
)


def test_create_groq_provider() -> None:
    """
    ProviderFactory should create GroqProvider.
    """

    factory = ProviderFactory(
        PlatformSettings(),
    )

    provider = factory.create(
        ProviderType.GROQ,
    )

    assert isinstance(
        provider,
        GroqProvider,
    )


def test_create_ollama_provider() -> None:
    """
    ProviderFactory should create OllamaProvider.
    """

    factory = ProviderFactory(
        PlatformSettings(),
    )

    provider = factory.create(
        ProviderType.OLLAMA,
    )

    assert isinstance(
        provider,
        OllamaProvider,
    )


def test_create_default_chat_provider() -> None:
    """
    Factory should create the configured default chat provider.
    """

    factory = ProviderFactory(
        PlatformSettings(),
    )

    provider = factory.create_default_chat_provider()

    assert isinstance(
        provider,
        GroqProvider,
    )


def test_create_default_embedding_provider() -> None:
    """
    Factory should create the configured embedding provider.
    """

    factory = ProviderFactory(
        PlatformSettings(),
    )

    provider = factory.create_default_embedding_provider()

    assert isinstance(
        provider,
        OllamaProvider,
    )


def test_create_default_reranking_provider() -> None:
    """
    Factory should create the configured reranking provider.
    """

    factory = ProviderFactory(
        PlatformSettings(),
    )

    provider = factory.create_default_reranking_provider()

    assert isinstance(
        provider,
        OllamaProvider,
    )


def test_create_unsupported_provider() -> None:
    """
    Unsupported providers should raise ProviderError.
    """

    factory = ProviderFactory(
        PlatformSettings(),
    )

    with pytest.raises(
        ProviderError,
    ):
        factory.create(
            ProviderType.OPENAI,
        )
