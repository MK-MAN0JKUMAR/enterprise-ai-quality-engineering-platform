# Application Module

## Purpose

The application module provides the business orchestration layer for the Enterprise AI Quality Engineering Platform.

It coordinates workflows while remaining independent of provider implementations, transport layers, and user interfaces.

---

## Responsibilities

- Define the shared application context.
- Define provider-independent application contracts.
- Standardize AI request models.
- Standardize AI response models.
- Define reusable application service abstractions.
- Define reusable use case abstractions.
- Provide the canonical interface between business logic and provider runtime implementations.

---

## Package Structure

```text
application/
├── context/
├── contracts/
├── services/
├── use_cases/
└── exceptions.py
```

---

## Application Contracts

The `contracts` package defines the canonical request and response models used throughout the platform.

These contracts are intentionally independent of any provider SDK and act as the communication boundary between the application layer and runtime providers.

Current contracts include:

- ChatRequest
- ChatResponse
- ChatMessage
- ChatChoice
- TokenUsage
- ChatGenerationOptions

All runtime providers are expected to translate provider-specific request and response models into these shared application contracts.

---

## Dependency Rules

The application layer may depend on:

- common
- config
- exceptions
- providers (interfaces only)
- providers (interfaces and abstractions only)
- Provider SDKs must never be imported directly into the application layer.

The application layer must not depend on:

- Ollama
- Groq
- OpenAI
- FastAPI
- CLI
- Streamlit
- Reporting
- Evaluation
- Retrieval

---

## Design Principles

- Framework independent
- Provider independent
- Transport independent
- Technology agnostic
- Single responsibility
- Dependency inversion

---

## Public API

- ApplicationContext
- ChatRequest
- ChatResponse
- ChatMessage
- ChatChoice
- TokenUsage
- ChatGenerationOptions
- ApplicationService
- UseCase
- ApplicationError

---

## Future Extensions

The following capabilities are expected to build on this module:

- Evaluation services
- Provider orchestration
- Dataset services
- Benchmark execution
- Reporting services
- Retrieval services
- Agent workflows
- API endpoints
- CLI commands
- UI workflows

No changes to the public API should introduce dependencies on concrete AI providers.

---

## Status

Implemented across the following feature branches:

- feature/application-services
- feature/ai-model-contracts
