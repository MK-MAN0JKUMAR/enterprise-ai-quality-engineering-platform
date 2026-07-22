"""
Ollama provider constants.
"""

from enterprise_ai_quality_engineering_platform.providers.capabilities import (
    ProviderCapability,
)

PROVIDER_NAME = "ollama"

PROVIDER_VENDOR = "Ollama"

PROVIDER_VERSION = "1.0"

SUPPORTED_CAPABILITIES: tuple[ProviderCapability, ...] = (
    ProviderCapability.CHAT,
    ProviderCapability.EMBEDDING,
)
