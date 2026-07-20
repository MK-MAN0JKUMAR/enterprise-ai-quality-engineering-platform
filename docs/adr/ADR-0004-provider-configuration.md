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

Introduce a dedicated configuration layer.

Configuration hierarchy:

PlatformSettings
→ ProviderSettings
→ ProviderFactory
→ Runtime Provider

Providers receive configuration through constructor injection.

ProviderFactory owns provider creation.

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

- Provider Registry
- Dynamic Provider Discovery
- Plugin Providers
- Runtime Switching
