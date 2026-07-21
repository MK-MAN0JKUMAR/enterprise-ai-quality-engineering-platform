"""
Provider abstractions.

This package defines the provider interfaces shared by all
LLM, embedding, reranking, and future AI providers.
"""

from .base import Provider
from .capabilities import ProviderCapability
from .exceptions import ProviderError
from .factory import ProviderFactory
from .gemini import GeminiProvider
from .groq import GroqProvider
from .ollama import OllamaProvider
from .registry import ProviderRegistry
from .types import ProviderMetadata

__all__ = [
    "Provider",
    "ProviderCapability",
    "ProviderError",
    "ProviderFactory",
    "ProviderRegistry",
    "ProviderMetadata",
    "GeminiProvider",
    "GroqProvider",
    "OllamaProvider",
]
