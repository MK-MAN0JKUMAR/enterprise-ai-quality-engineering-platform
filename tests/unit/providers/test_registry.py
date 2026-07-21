"""
Tests for ProviderRegistry.
"""

import pytest

from enterprise_ai_testing_platform.common import ProviderType
from enterprise_ai_testing_platform.config import PlatformSettings
from enterprise_ai_testing_platform.providers import (
    GeminiProvider,
    GroqProvider,
    OllamaProvider,
    ProviderRegistry,
)


def test_contains_registered_provider() -> None:
    """
    Registered providers should be discoverable.
    """

    assert ProviderRegistry.contains(ProviderType.GROQ)
    assert ProviderRegistry.contains(ProviderType.GEMINI)
    assert ProviderRegistry.contains(ProviderType.OLLAMA)


def test_contains_unregistered_provider() -> None:
    """
    Unknown providers should not exist in the registry.
    """

    assert not ProviderRegistry.contains(
        ProviderType.OPENAI,
    )


def test_create_groq_provider() -> None:
    """
    Registry should create a Groq provider.
    """

    provider = ProviderRegistry.create(
        ProviderType.GROQ,
        PlatformSettings(),
    )

    assert isinstance(
        provider,
        GroqProvider,
    )


def test_create_gemini_provider() -> None:
    """
    Registry should create a Gemini provider.
    """

    provider = ProviderRegistry.create(
        ProviderType.GEMINI,
        PlatformSettings(),
    )

    assert isinstance(
        provider,
        GeminiProvider,
    )


def test_create_ollama_provider() -> None:
    """
    Registry should create an Ollama provider.
    """

    provider = ProviderRegistry.create(
        ProviderType.OLLAMA,
        PlatformSettings(),
    )

    assert isinstance(
        provider,
        OllamaProvider,
    )


def test_create_unknown_provider_raises_key_error() -> None:
    """
    Unknown providers should raise KeyError.
    """

    with pytest.raises(KeyError):
        ProviderRegistry.create(
            ProviderType.OPENAI,
            PlatformSettings(),
        )


def test_registered_providers() -> None:
    """
    Registry should expose all registered providers.
    """

    providers = ProviderRegistry.registered_providers()

    assert ProviderType.GROQ in providers
    assert ProviderType.GEMINI in providers
    assert ProviderType.OLLAMA in providers
