from enterprise_ai_testing_platform.providers import ProviderCapability
from enterprise_ai_testing_platform.providers.groq import GroqProvider


def test_groq_provider_lifecycle() -> None:
    provider = GroqProvider()

    assert provider.is_initialized is False

    provider.initialize()

    assert provider.is_initialized is True

    provider.shutdown()

    assert provider.is_initialized is False


def test_groq_provider_metadata() -> None:
    provider = GroqProvider()

    metadata = provider.metadata

    assert metadata.name == "groq"
    assert metadata.vendor == "Groq"
    assert metadata.version == "1.0"

    assert metadata.capabilities == (ProviderCapability.CHAT,)
