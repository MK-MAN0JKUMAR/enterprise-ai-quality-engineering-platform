# Application Contracts Diagram

## Overview

This diagram illustrates how the Application Contract layer separates business logic from provider-specific implementations.

The application layer communicates only through provider-independent contracts. Runtime providers are responsible for translating between these contracts and provider-specific SDKs or APIs.

---

# High-Level Architecture

```text
                        Enterprise AI Quality Engineering Platform

┌─────────────────────────────────────────────────────────────────────────────┐
│                           Application Layer                                 │
│                                                                             │
│  • Services                                                                  │
│  • Use Cases                                                                 │
│  • Application Context                                                       │
└───────────────────────────────┬─────────────────────────────────────────────┘
                                │
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                      Provider-Independent Contracts                          │
│                                                                             │
│  • ChatRequest                                                               │
│  • ChatResponse                                                              │
│  • ChatMessage                                                               │
│  • ChatChoice                                                                │
│  • TokenUsage                                                                │
│  • ChatGenerationOptions                                                     │
└───────────────────────────────┬─────────────────────────────────────────────┘
                                │
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                         Provider Runtime Layer                               │
│                                                                             │
│  • Request Mapping                                                           │
│  • Response Mapping                                                          │
│  • Validation                                                                │
│  • Error Handling                                                            │
│  • Runtime Execution                                                         │
└───────────────────────────────┬─────────────────────────────────────────────┘
                                │
        ┌───────────────────────┼────────────────────────┐
        │                       │                        │
        ▼                       ▼                        ▼
┌───────────────┐      ┌────────────────┐      ┌────────────────┐
│ Groq Provider │      │ Gemini Provider│      │ Ollama Provider│
└───────────────┘      └────────────────┘      └────────────────┘
        │                       │                        │
        └───────────────┬───────┴───────────────┬────────┘
                        │                       │
                        ▼                       ▼
               ┌────────────────┐      ┌────────────────┐
               │ LM Studio      │      │ Future Provider│
               └────────────────┘      └────────────────┘
