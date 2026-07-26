"""
Provider-agnostic AI chat domain models.

These immutable domain models define the shared request and response
contracts used across provider execution, evaluation, benchmarking,
retrieval, reporting, and future AI platform capabilities.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from enterprise_ai_quality_engineering_platform.common import (
    FinishReason,
    JsonDict,
    MessageRole,
)


@dataclass(frozen=True, slots=True, kw_only=True)
class ChatMessage:
    """
    Represents a single chat message.
    """

    role: MessageRole

    content: str

    name: str | None = None

    tool_call_id: str | None = None

    metadata: JsonDict = field(default_factory=dict)

    def __post_init__(self) -> None:
        """
        Validate the chat message.
        """

        if self.role is not MessageRole.TOOL and not self.content.strip():
            raise ValueError("Message content cannot be empty.")


@dataclass(frozen=True, slots=True, kw_only=True)
class ChatGenerationOptions:
    """
    Model generation configuration.
    """

    temperature: float | None = None

    top_p: float | None = None

    max_tokens: int | None = None

    stop_sequences: tuple[str, ...] = ()

    seed: int | None = None

    frequency_penalty: float | None = None

    presence_penalty: float | None = None

    metadata: JsonDict = field(default_factory=dict)

    def __post_init__(self) -> None:
        """
        Validate generation options.
        """
        if self.temperature is not None and not 0.0 <= self.temperature <= 2.0:
            raise ValueError("temperature must be between 0.0 and 2.0.")

        if self.top_p is not None and not 0.0 <= self.top_p <= 1.0:
            raise ValueError("top_p must be between 0.0 and 1.0.")

        if self.max_tokens is not None and self.max_tokens <= 0:
            raise ValueError("max_tokens must be greater than zero.")

        if self.frequency_penalty is not None and not -2.0 <= self.frequency_penalty <= 2.0:
            raise ValueError("frequency_penalty must be between -2.0 and 2.0.")

        if self.presence_penalty is not None and not -2.0 <= self.presence_penalty <= 2.0:
            raise ValueError("presence_penalty must be between -2.0 and 2.0.")


@dataclass(frozen=True, slots=True, kw_only=True)
class ChatRequest:
    """
    Provider-agnostic chat request.
    """

    messages: tuple[ChatMessage, ...]

    model: str

    options: ChatGenerationOptions | None = None

    request_id: str | None = None

    metadata: JsonDict = field(default_factory=dict)

    def __post_init__(self) -> None:
        """
        Validate the chat request.
        """
        if not self.messages:
            raise ValueError("A chat request must contain at least one message.")

        if not self.model.strip():
            raise ValueError("Model name cannot be empty.")


@dataclass(frozen=True, slots=True, kw_only=True)
class TokenUsage:
    """
    Provider-neutral token usage statistics.
    """

    input_tokens: int = 0

    output_tokens: int = 0

    total_tokens: int = 0

    metadata: JsonDict = field(default_factory=dict)

    def __post_init__(self) -> None:
        """
        Validate token usage.
        """
        if self.input_tokens < 0:
            raise ValueError("input_tokens cannot be negative.")

        if self.output_tokens < 0:
            raise ValueError("output_tokens cannot be negative.")

        if self.total_tokens < 0:
            raise ValueError("total_tokens cannot be negative.")

        expected_total = self.input_tokens + self.output_tokens

        if self.total_tokens == 0:
            object.__setattr__(
                self,
                "total_tokens",
                expected_total,
            )
        elif self.total_tokens != expected_total:
            raise ValueError("total_tokens must equal input_tokens + output_tokens.")


@dataclass(frozen=True, slots=True, kw_only=True)
class ChatChoice:
    """
    Represents one generated response.
    """

    index: int

    message: ChatMessage

    finish_reason: FinishReason

    logprobs: JsonDict | None = None

    metadata: JsonDict = field(default_factory=dict)

    def __post_init__(self) -> None:
        """
        Validate the chat choice.
        """
        if self.index < 0:
            raise ValueError("Choice index cannot be negative.")


@dataclass(frozen=True, slots=True, kw_only=True)
class ChatResponse:
    """
    Provider-agnostic chat response.
    """

    model: str

    choices: tuple[ChatChoice, ...]

    response_id: str | None = None

    usage: TokenUsage | None = None

    created: int | None = None

    metadata: JsonDict = field(default_factory=dict)

    def __post_init__(self) -> None:
        """
        Validate the chat response.
        """
        if not self.model.strip():
            raise ValueError("Model name cannot be empty.")

        if not self.choices:
            raise ValueError("A chat response must contain at least one choice.")

        if self.created is not None and self.created < 0:
            raise ValueError("created timestamp cannot be negative.")
