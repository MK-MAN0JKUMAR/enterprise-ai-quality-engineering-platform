# ADR-0003: Clean Architecture

- **Status:** Accepted
- **Date:** 2026-07-13
- **Decision Makers:** Project Owner

---

# Context

The Enterprise AI Testing Platform is intended to evolve over multiple years and support a wide range of AI quality engineering capabilities, including LLM testing, prompt evaluation, RAG evaluation, agent evaluation, benchmarking, observability, reporting, and plugin-based extensions.

The AI ecosystem evolves rapidly. New providers, SDKs, vector databases, evaluation frameworks, and deployment platforms appear frequently. Directly coupling business logic to these technologies would make the platform difficult to maintain and expensive to evolve.

To ensure long-term maintainability and extensibility, the platform requires an architecture that isolates business logic from infrastructure and external dependencies.

---

# Decision

The project will adopt **Clean Architecture** as its primary architectural style.

Business rules must remain independent of:

- LLM providers
- Embedding providers
- Vector databases
- Storage technologies
- User interfaces
- APIs
- Frameworks
- Third-party SDKs
- Infrastructure implementations

Dependencies must always point toward the core business domain.

The core domain must never depend on infrastructure code.

---

# Architectural Overview

```text
                User Interfaces
      (CLI, API, Dashboard, Future UI)

                     │
                     ▼

            Application Services
        (Use Cases / Orchestration)

                     │
                     ▼

              Core Domain Layer
     (Business Rules & Interfaces)

                     ▲
                     │

       Infrastructure Implementations

   Providers
   Plugins
   Storage
   Retrieval
   Reporting
   Logging
   Security
   Integrations
```

---

# Dependency Rule

The most important rule is:

**Source code dependencies must always point inward toward the Core Domain.**

The Core Domain must not import or depend on infrastructure implementations.

Examples of infrastructure components include:

- Ollama
- Groq
- OpenAI
- Playwright
- FAISS
- Chroma
- FastAPI
- LangChain
- LiteLLM
- DeepEval
- RAGAS

These technologies may change over time.

The Core Domain should remain unaffected by such changes.

---

# Architectural Layers

## Core Domain

The Core Domain contains:

- Domain models
- Business rules
- Interfaces
- Contracts
- Exceptions
- Value objects
- Shared abstractions

The Core Domain represents the stable center of the platform.

---

## Application Layer

The Application Layer coordinates business operations.

Responsibilities include:

- Workflow orchestration
- Use cases
- Execution pipelines
- Service coordination

Application services should contain minimal business rules.

---

## Infrastructure Layer

Infrastructure provides concrete implementations.

Examples include:

- LLM providers
- Embedding providers
- Vector databases
- Reporting engines
- Logging
- Storage
- Plugin loading
- External APIs

Infrastructure depends on interfaces defined by the Core Domain.

---

## Presentation Layer

Responsible for interacting with users.

Examples:

- CLI
- REST APIs
- Web Dashboard
- Future Desktop UI

Presentation should never contain business logic.

---

# Provider Abstraction

Every external provider must implement a common interface.

Example categories include:

- LLM Providers
- Embedding Providers
- Vector Database Providers
- Storage Providers
- Authentication Providers

Business logic interacts only with provider interfaces.

Provider-specific SDKs remain isolated within infrastructure modules.

---

# Plugin Architecture

Optional functionality should be implemented through plugins rather than modifying the Core Domain.

Examples include:

- Custom evaluation metrics
- New providers
- Additional reports
- External integrations

Plugins extend the platform without introducing tight coupling.

---

# Configuration Strategy

Configuration must remain external to business logic.

Configuration values may originate from:

- Environment variables
- Configuration files
- CLI arguments

Business logic should receive configuration through dependency injection rather than reading configuration directly.

---

# Dependency Injection

Object creation should remain separate from business logic.

Dependencies should be supplied through constructors, factories, or dependency injection mechanisms.

Business objects should never instantiate infrastructure implementations directly.

---

# Design Principles

The architecture follows the following engineering principles:

- Separation of Concerns
- Dependency Inversion Principle
- Single Responsibility Principle
- Interface Segregation Principle
- Open/Closed Principle
- High Cohesion
- Low Coupling
- Composition over Inheritance

These principles apply across every module in the repository.

---

# Consequences

Positive consequences:

- Easier testing
- Provider independence
- Framework independence
- Reduced vendor lock-in
- Improved maintainability
- Better scalability
- Cleaner module boundaries
- Easier future refactoring
- Simpler plugin integration

Trade-offs:

- Increased number of abstractions
- Additional interfaces
- More architectural planning
- Slightly slower initial development

These trade-offs are acceptable because long-term maintainability is the primary objective of the project.

---

# Alternatives Considered

## Layered Architecture

Rejected.

Traditional layered architectures often allow business logic to become tightly coupled with infrastructure.

---

## MVC

Rejected.

MVC is well suited for user interface applications but does not provide sufficient separation for a modular AI engineering platform.

---

## Direct Provider Integration

Rejected.

Allowing business logic to communicate directly with provider SDKs would create vendor lock-in and significantly increase maintenance costs.

---

## Microservices

Rejected for the initial implementation.

The project will begin as a modular monolith.

If future scalability requirements justify decomposition, modules can later be extracted into independent services with minimal architectural changes.

---

# Architectural Rules

The following rules are mandatory:

1. Business logic must not depend on infrastructure.

2. Infrastructure depends on interfaces defined by the Core Domain.

3. External SDKs must remain isolated within provider implementations.

4. User interfaces must not contain business logic.

5. Configuration must remain external to business logic.

6. Every module must have a single, clearly defined responsibility.

7. Shared abstractions belong in the Core Domain.

8. New capabilities should extend existing abstractions rather than modify stable business rules.

9. Prefer composition over inheritance.

10. Architecture takes precedence over implementation convenience.

---

# Future Evolution

The architecture is expected to support future capabilities including:

- Additional AI providers
- New evaluation frameworks
- New vector databases
- Knowledge graph retrieval
- Multi-modal AI
- Distributed execution
- Cloud deployment
- Enterprise authentication
- Multi-tenancy
- Plugin ecosystem

These additions should require new infrastructure implementations rather than changes to the Core Domain.

---

# References

- ADR-0001: Project Vision
- ADR-0002: Repository Structure
