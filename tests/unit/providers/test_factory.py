"""
Tests for ProviderFactory.
"""

import pytest

from enterprise_ai_testing_platform.common import ProviderType
from enterprise_ai_testing_platform.config import PlatformSettings
from enterprise_ai_testing_platform.providers import (
    GeminiProvider,
    GroqProvider,
    OllamaProvider,
    ProviderFactory,
)
from enterprise_ai_testing_platform.providers.exceptions import (
    ProviderError,
)
from enterprise_ai_testing_platform.providers.lmstudio.provider import LMStudioProvider


def test_create_groq_provider() -> None:
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


def test_create_gemini_provider() -> None:
    factory = ProviderFactory(
        PlatformSettings(),
    )

    provider = factory.create(
        ProviderType.GEMINI,
    )

    assert isinstance(
        provider,
        GeminiProvider,
    )


def test_create_ollama_provider() -> None:
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
    factory = ProviderFactory(
        PlatformSettings(),
    )

    provider = factory.create_default_chat_provider()

    assert isinstance(
        provider,
        GroqProvider,
    )


def test_create_default_embedding_provider() -> None:
    factory = ProviderFactory(
        PlatformSettings(),
    )

    provider = factory.create_default_embedding_provider()

    assert isinstance(
        provider,
        OllamaProvider,
    )


def test_create_default_reranking_provider() -> None:
    factory = ProviderFactory(
        PlatformSettings(),
    )

    provider = factory.create_default_reranking_provider()

    assert isinstance(
        provider,
        OllamaProvider,
    )


def test_create_unsupported_provider() -> None:
    factory = ProviderFactory(
        PlatformSettings(),
    )

    with pytest.raises(
        ProviderError,
        match="Unsupported provider",
    ):
        factory.create(
            ProviderType.OPENAI,
        )


def test_factory_creates_lmstudio_provider() -> None:
    """
    Factory should create LM Studio provider.
    """

    factory = ProviderFactory(
        PlatformSettings(),
    )

    provider = factory.create(
        ProviderType.LMSTUDIO,
    )

    assert isinstance(
        provider,
        LMStudioProvider,
    )
