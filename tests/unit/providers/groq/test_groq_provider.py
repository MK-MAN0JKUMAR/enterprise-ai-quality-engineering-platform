from enterprise_ai_quality_engineering_platform.config.providers import GroqSettings
from enterprise_ai_quality_engineering_platform.providers.groq import GroqProvider


def test_groq_provider_lifecycle() -> None:
    settings = GroqSettings()

    provider = GroqProvider(settings)

    assert provider.is_initialized is False

    provider.initialize()

    assert provider.is_initialized is True

    provider.shutdown()

    assert provider.is_initialized is False


def test_groq_provider_metadata() -> None:
    settings = GroqSettings()

    provider = GroqProvider(settings)

    metadata = provider.metadata

    assert metadata.name == "groq"

    assert metadata.vendor == "Groq"

    assert metadata.version == "1.0"

    assert len(metadata.capabilities) == 1
