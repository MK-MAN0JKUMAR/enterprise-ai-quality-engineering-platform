"""
Service lifetime definitions.
"""

from enum import StrEnum


class ServiceLifetime(StrEnum):
    """
    Supported service lifetimes.
    """

    SINGLETON = "singleton"
    TRANSIENT = "transient"
