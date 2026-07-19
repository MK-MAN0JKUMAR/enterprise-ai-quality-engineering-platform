"""
Application response contracts.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from enterprise_ai_testing_platform.common.types import JsonDict


@dataclass(slots=True)
class ApplicationResponse:
    """
    Base application response.
    """

    success: bool = True

    metadata: JsonDict = field(default_factory=dict)
