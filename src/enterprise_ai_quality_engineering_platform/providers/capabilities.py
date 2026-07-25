"""
Provider capability definitions.
"""

from enum import StrEnum


class ProviderCapability(StrEnum):
    """
    Supported provider capabilities.
    """

    CHAT = "chat"

    EMBEDDING = "embedding"

    RERANKING = "reranking"

    MODERATION = "moderation"

    IMAGE_GENERATION = "image_generation"

    SPEECH_TO_TEXT = "speech_to_text"

    TEXT_TO_SPEECH = "text_to_speech"
