"""
Enterprise AI Testing Platform.

An enterprise-grade, modular platform for testing and evaluating AI systems,
including Large Language Models (LLMs), Retrieval-Augmented Generation (RAG)
pipelines, AI agents, prompts, and AI-powered applications.

This package provides the core architecture and shared infrastructure used
throughout the platform.
"""

from __future__ import annotations

from .core.metadata import VERSION

__version__ = VERSION

__all__ = ["__version__"]
