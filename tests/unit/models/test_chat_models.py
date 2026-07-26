"""
Tests for chat model contracts.
"""

from dataclasses import FrozenInstanceError

import pytest

from enterprise_ai_quality_engineering_platform.common import (
    FinishReason,
    MessageRole,
)
from enterprise_ai_quality_engineering_platform.models import (
    ChatChoice,
    ChatGenerationOptions,
    ChatMessage,
    ChatRequest,
    ChatResponse,
    TokenUsage,
)


def test_chat_message_defaults() -> None:
    message = ChatMessage(
        role=MessageRole.USER,
        content="Hello",
    )

    assert message.role is MessageRole.USER
    assert message.content == "Hello"
    assert message.name is None
    assert message.metadata == {}


def test_generation_options_defaults() -> None:
    options = ChatGenerationOptions()

    assert options.temperature is None
    assert options.top_p is None
    assert options.max_tokens is None
    assert options.stop_sequences == ()
    assert options.seed is None
    assert options.frequency_penalty is None
    assert options.presence_penalty is None
    assert options.metadata == {}


def test_chat_request() -> None:
    message = ChatMessage(
        role=MessageRole.USER,
        content="Hello",
    )

    request = ChatRequest(
        model="llama3",
        messages=(message,),
    )

    assert request.model == "llama3"
    assert len(request.messages) == 1
    assert request.options is None
    assert request.metadata == {}


def test_token_usage() -> None:
    usage = TokenUsage(
        input_tokens=10,
        output_tokens=20,
        total_tokens=30,
    )

    assert usage.input_tokens == 10
    assert usage.output_tokens == 20
    assert usage.total_tokens == 30
    assert usage.metadata == {}


def test_chat_choice() -> None:
    message = ChatMessage(
        role=MessageRole.ASSISTANT,
        content="Hi",
    )

    choice = ChatChoice(
        index=0,
        message=message,
        finish_reason=FinishReason.STOP,
    )

    assert choice.index == 0
    assert choice.finish_reason is FinishReason.STOP


def test_chat_response() -> None:
    message = ChatMessage(
        role=MessageRole.ASSISTANT,
        content="Hi",
    )

    choice = ChatChoice(
        index=0,
        message=message,
        finish_reason=FinishReason.STOP,
    )

    usage = TokenUsage(
        input_tokens=10,
        output_tokens=20,
        total_tokens=30,
    )

    response = ChatResponse(
        model="llama3",
        choices=(choice,),
        usage=usage,
    )

    assert response.model == "llama3"
    assert len(response.choices) == 1
    assert response.usage == usage


def test_chat_message_is_frozen() -> None:
    message = ChatMessage(
        role=MessageRole.USER,
        content="Hello",
    )

    with pytest.raises(FrozenInstanceError):
        message.content = "Updated"  # type: ignore[misc]


def test_chat_message_keyword_only() -> None:
    message = ChatMessage(
        role=MessageRole.USER,
        content="Hello",
    )

    assert message.role is MessageRole.USER


def test_chat_response_response_id() -> None:
    message = ChatMessage(
        role=MessageRole.ASSISTANT,
        content="Hi",
    )

    choice = ChatChoice(
        index=0,
        message=message,
        finish_reason=FinishReason.STOP,
    )

    response = ChatResponse(
        response_id="resp-001",
        model="llama3",
        choices=(choice,),
    )

    assert response.response_id == "resp-001"


def test_chat_request_requires_messages() -> None:
    with pytest.raises(ValueError):
        ChatRequest(
            model="llama3",
            messages=(),
        )


def test_chat_request_requires_model() -> None:
    message = ChatMessage(
        role=MessageRole.USER,
        content="Hello",
    )

    with pytest.raises(ValueError):
        ChatRequest(
            model="",
            messages=(message,),
        )


def test_generation_options_invalid_temperature() -> None:
    with pytest.raises(ValueError):
        ChatGenerationOptions(
            temperature=3.0,
        )


def test_generation_options_invalid_top_p() -> None:
    with pytest.raises(ValueError):
        ChatGenerationOptions(
            top_p=2.0,
        )


def test_generation_options_invalid_max_tokens() -> None:
    with pytest.raises(ValueError):
        ChatGenerationOptions(
            max_tokens=0,
        )


def test_token_usage_negative_values() -> None:
    with pytest.raises(ValueError):
        TokenUsage(
            input_tokens=-1,
        )


def test_chat_choice_negative_index() -> None:
    message = ChatMessage(
        role=MessageRole.ASSISTANT,
        content="Hello",
    )

    with pytest.raises(ValueError):
        ChatChoice(
            index=-1,
            message=message,
            finish_reason=FinishReason.STOP,
        )


def test_chat_message_requires_content() -> None:
    with pytest.raises(ValueError):
        ChatMessage(
            role=MessageRole.USER,
            content="",
        )


def test_token_usage_calculates_total():
    usage = TokenUsage(
        input_tokens=10,
        output_tokens=20,
    )

    assert usage.total_tokens == 30
