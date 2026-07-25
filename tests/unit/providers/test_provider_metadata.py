from enterprise_ai_quality_engineering_platform.providers import (
    ProviderCapability,
    ProviderMetadata,
)


def test_provider_metadata() -> None:
    metadata = ProviderMetadata(
        name="groq",
        vendor="Groq",
        version="1.0",
        capabilities=(ProviderCapability.CHAT,),
    )

    assert metadata.name == "groq"
    assert metadata.vendor == "Groq"
    assert metadata.version == "1.0"
    assert metadata.capabilities == (ProviderCapability.CHAT,)
