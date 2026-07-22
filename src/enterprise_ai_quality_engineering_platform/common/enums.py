"""
Shared enumerations.
"""

from enum import StrEnum


class Environment(StrEnum):
    """
    Application environments.
    """

    DEVELOPMENT = "development"
    TESTING = "testing"
    STAGING = "staging"
    PRODUCTION = "production"


class LogLevel(StrEnum):
    """
    Supported log levels.
    """

    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


class ProviderType(StrEnum):
    """
    Supported AI providers.
    """

    GROQ = "groq"

    OLLAMA = "ollama"

    OPENAI = "openai"

    GEMINI = "gemini"

    LMSTUDIO = "lmstudio"

    ANTHROPIC = "anthropic"

    AZURE_OPENAI = "azure_openai"

    HUGGINGFACE = "huggingface"

    BEDROCK = "bedrock"

    VERTEX_AI = "vertex_ai"

    CUSTOM = "custom"
