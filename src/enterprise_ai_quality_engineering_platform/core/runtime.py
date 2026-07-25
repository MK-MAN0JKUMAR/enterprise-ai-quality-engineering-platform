"""
Runtime helpers.
"""

from __future__ import annotations

import platform
import sys

from .metadata import (
    PACKAGE_NAME,
    PROJECT_NAME,
    PYTHON_MIN_VERSION,
    VERSION,
)


def python_version() -> str:
    """Return the current Python version."""

    return platform.python_version()


def platform_name() -> str:
    """Return the operating system name."""

    return platform.system()


def validate_python_version() -> None:
    """Validate the running Python version."""

    if sys.version_info < PYTHON_MIN_VERSION:
        required = ".".join(map(str, PYTHON_MIN_VERSION))
        current = platform.python_version()

        raise RuntimeError(
            f"{PROJECT_NAME} requires Python {required} or newer. Current version: {current}"
        )


def runtime_metadata() -> dict[str, str]:
    """Return runtime metadata."""

    return {
        "project": PROJECT_NAME,
        "package": PACKAGE_NAME,
        "version": VERSION,
        "python": python_version(),
        "platform": platform_name(),
    }
