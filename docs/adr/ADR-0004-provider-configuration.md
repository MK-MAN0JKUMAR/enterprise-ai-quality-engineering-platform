# ADR-0004

# Title

Provider Configuration Architecture

---

## Status

Accepted

---

## Context

The platform supports multiple LLM providers.

Each provider requires:

- API configuration
- Models
- Runtime configuration
- Future extensibility

Provider implementations should remain independent from configuration loading.

---

## Decision

Introduce a dedicated provider architecture composed of:

PlatformSettings
→ ProviderSettings
→ ProviderFactory
→ ProviderRegistry
→ Runtime Provider

Responsibilities are separated as follows:

- ProviderSettings owns provider configuration.
- ProviderFactory remains the public entry point for provider creation.
- ProviderRegistry owns provider registration and runtime implementation lookup.
- Runtime providers receive configuration through constructor injection.

This keeps provider creation centralized while allowing new providers to be added with minimal impact to the factory.

---

## Consequences

### Advantages

- Clean separation
- Testable
- Dependency Injection
- Easy to extend
- Future cloud providers
- Environment driven

### Disadvantages

- Slightly more abstraction
- Additional configuration models

---

## Alternatives Considered

### Global Configuration Singleton

Rejected.

Reasons:

- Hidden dependencies
- Difficult testing
- Tight coupling

---

### Provider Reads Environment Variables

Rejected.

Reasons:

- Violates SRP
- Hard to mock
- Runtime coupled to configuration

---

## Future Work

- Dynamic provider discovery
- Plugin-based providers
- Runtime provider switching
- Health monitoring
- Provider failover
