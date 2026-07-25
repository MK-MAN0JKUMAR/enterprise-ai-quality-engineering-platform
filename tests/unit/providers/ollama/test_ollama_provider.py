from enterprise_ai_quality_engineering_platform.config.providers import OllamaSettings
from enterprise_ai_quality_engineering_platform.providers.ollama import OllamaProvider


def test_ollama_provider_lifecycle() -> None:
    settings = OllamaSettings()

    provider = OllamaProvider(settings)

    assert provider.is_initialized is False

    provider.initialize()

    assert provider.is_initialized is True

    provider.shutdown()

    assert provider.is_initialized is False


def test_ollama_provider_metadata() -> None:
    settings = OllamaSettings()

    provider = OllamaProvider(settings)

    metadata = provider.metadata

    assert metadata.name == "ollama"

    assert metadata.vendor == "Ollama"

    assert metadata.version == "1.0"

    assert len(metadata.capabilities) == 2
