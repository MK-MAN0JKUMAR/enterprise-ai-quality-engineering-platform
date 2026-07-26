"""
Shared AI model contracts.

These immutable domain models define the provider-agnostic
contracts shared across the platform.
"""

from .chat import (
    ChatChoice,
    ChatGenerationOptions,
    ChatMessage,
    ChatRequest,
    ChatResponse,
    TokenUsage,
)

__all__ = [
    "ChatChoice",
    "ChatMessage",
    "ChatRequest",
    "ChatResponse",
    "ChatGenerationOptions",
    "TokenUsage",
]
