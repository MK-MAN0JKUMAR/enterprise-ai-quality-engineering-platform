"""
Application response contracts.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from enterprise_ai_quality_engineering_platform.common import JsonDict
from enterprise_ai_quality_engineering_platform.models import (
    ChatChoice,
    ChatResponse,
    TokenUsage,
)


@dataclass(frozen=True, slots=True, kw_only=True)
class ApplicationResponse:
    """
    Base response contract for all application use cases.
    """

    success: bool = True

    metadata: JsonDict = field(default_factory=dict)


__all__ = [
    "ApplicationResponse",
    "ChatChoice",
    "TokenUsage",
    "ChatResponse",
]
