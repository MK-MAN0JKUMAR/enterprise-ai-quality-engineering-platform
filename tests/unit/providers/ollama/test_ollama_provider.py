from enterprise_ai_testing_platform.providers import ProviderCapability
from enterprise_ai_testing_platform.providers.ollama import OllamaProvider


def test_ollama_provider_lifecycle() -> None:
    provider = OllamaProvider()

    assert provider.is_initialized is False

    provider.initialize()

    assert provider.is_initialized is True

    provider.shutdown()

    assert provider.is_initialized is False


def test_ollama_provider_metadata() -> None:
    provider = OllamaProvider()

    metadata = provider.metadata

    assert metadata.name == "ollama"
    assert metadata.vendor == "Ollama"
    assert metadata.version == "1.0"

    assert metadata.capabilities == (
        ProviderCapability.CHAT,
        ProviderCapability.EMBEDDING,
    )
