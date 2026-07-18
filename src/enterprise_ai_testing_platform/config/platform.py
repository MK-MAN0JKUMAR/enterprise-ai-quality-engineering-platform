"""
Root configuration model.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

from .application import ApplicationSettings
from .runtime import RuntimeSettings


class PlatformSettings(BaseModel):
    """Root platform configuration."""

    model_config = ConfigDict(
        frozen=True,
    )

    application: ApplicationSettings = Field(
        default_factory=ApplicationSettings,
    )

    runtime: RuntimeSettings = Field(
        default_factory=RuntimeSettings,
    )
