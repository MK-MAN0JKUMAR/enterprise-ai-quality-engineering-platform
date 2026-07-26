"""
Application request contracts.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from enterprise_ai_quality_engineering_platform.common import JsonDict
from enterprise_ai_quality_engineering_platform.models import (
    ChatGenerationOptions,
    ChatMessage,
    ChatRequest,
)


@dataclass(frozen=True, slots=True, kw_only=True)
class ApplicationRequest:
    """
    Base request contract for all application use cases.
    """

    metadata: JsonDict = field(default_factory=dict)


__all__ = [
    "ApplicationRequest",
    "ChatMessage",
    "ChatGenerationOptions",
    "ChatRequest",
]
