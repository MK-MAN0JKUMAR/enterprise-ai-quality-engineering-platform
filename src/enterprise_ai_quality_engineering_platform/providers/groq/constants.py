"""
Groq provider constants.
"""

from enterprise_ai_quality_engineering_platform.providers.capabilities import (
    ProviderCapability,
)

PROVIDER_NAME = "groq"

PROVIDER_VENDOR = "Groq"

PROVIDER_VERSION = "1.0"

SUPPORTED_CAPABILITIES: tuple[ProviderCapability, ...] = (ProviderCapability.CHAT,)
