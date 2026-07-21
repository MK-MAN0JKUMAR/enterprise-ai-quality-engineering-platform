# Provider Configuration

## Overview

The Enterprise AI Testing Platform supports multiple Large Language Model (LLM) providers through a configuration-driven architecture.

The configuration layer is responsible for:

- Provider selection
- Runtime configuration
- Environment variable mapping
- Default provider management
- Dependency injection

Runtime providers remain independent of configuration concerns.

---

# Architecture

```
                 PlatformSettings
                        │
                        ▼
                 ProviderSettings
                        │
                        ▼
                 ProviderFactory
                        │
                        ▼
                 ProviderRegistry
          ┌─────────────┼─────────────┐
          ▼             ▼             ▼
    GroqProvider   GeminiProvider  OllamaProvider
```

---

# Configuration Hierarchy

```
PlatformSettings
│
├── ApplicationSettings
├── RuntimeSettings
├── LoggingSettings
└── ProviderSettings
    ├── GroqSettings
    ├── GeminiSettings
    └── OllamaSettings
```

---

# Environment Variables

## Default Providers

| Variable | Description |
|-----------|-------------|
| EATP_PROVIDER_DEFAULT_CHAT_PROVIDER | Default chat provider |
| EATP_PROVIDER_DEFAULT_EMBEDDING_PROVIDER | Default embedding provider |
| EATP_PROVIDER_DEFAULT_RERANKING_PROVIDER | Default reranking provider |
| EATP_GEMINI_API_KEY |
| EATP_GEMINI_BASE_URL |
| EATP_GEMINI_CHAT_MODEL |

---

## Groq

| Variable |
|-----------|
| EATP_GROQ_API_KEY |
| EATP_GROQ_BASE_URL |
| EATP_GROQ_CHAT_MODEL |

---

## Ollama

| Variable |
|-----------|
| EATP_OLLAMA_BASE_URL |
| EATP_OLLAMA_CHAT_MODEL |
| EATP_OLLAMA_EMBEDDING_MODEL |
| EATP_OLLAMA_RERANKING_MODEL |

---

# ProviderFactory

The ProviderFactory is responsible for constructing runtime provider instances using dependency injection.

Responsibilities:

- Create providers
- Inject provider configuration
- Select default providers
- Isolate provider creation logic

---

# ProviderRegistry

ProviderRegistry maintains the mapping between supported provider
types and their runtime implementations.

Responsibilities:

- Centralize provider registration
- Create runtime providers
- Expose registered providers
- Keep ProviderFactory independent of individual provider implementations

ProviderFactory delegates provider creation to ProviderRegistry while
remaining the public entry point for application code.

---


# Dependency Injection

Providers receive configuration via constructor injection.

Example:

```python
provider = GroqProvider(settings.providers.groq)
```

Providers never load configuration directly.

---

# Supported Providers

| Provider | Status |
|----------|--------|
| Groq | DONE |
| Ollama | DONE |
| OpenAI | Planned |
| Gemini | Planned |
| Anthropic | Planned |
| Azure OpenAI | Planned |

---

# Adding a New Provider

1. Create configuration model.
2. Add defaults.
3. Implement runtime provider.
4. Register in ProviderRegistry.
5. Add tests.
6. Update documentation.

---

# Design Principles

- Clean Architecture
- Dependency Injection
- Separation of Concerns
- Provider Independence
- Configuration-driven Runtime
- Open/Closed Principle
