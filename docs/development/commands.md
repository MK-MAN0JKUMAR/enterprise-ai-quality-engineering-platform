# Development Commands

This document contains the standard commands used while developing the Enterprise AI Testing Platform.

---

# Environment

## Sync Dependencies

```bash
uv sync
```

Install or synchronize all project dependencies from `pyproject.toml`.

---

## Verify Python Version

```bash
uv run python --version
```

---

## Create Virtual Environment

```bash
uv venv
```

---

# Code Quality

## Lint

```bash
uv run ruff check .
```

---

## Auto Fix Lint Issues

```bash
uv run ruff check . --fix
```

---

## Format Code

```bash
uv run black .
```

---

## Verify Formatting

```bash
uv run black --check .
```

---

## Type Checking

```bash
uv run mypy src
```

---

# Testing

## Run All Tests

```bash
uv run pytest
```

---

## Run a Single Test File

```bash
uv run pytest tests/unit/test_package.py
```

---

## Run Tests Matching a Keyword

```bash
uv run pytest -k package
```

---

# Pre-Commit

## Install Git Hooks

```bash
uv run pre-commit install
```

---

## Run All Hooks

```bash
uv run pre-commit run --all-files
```

---

# Package Verification

Verify the package imports successfully.

```bash
uv run python -c "import enterprise_ai_testing_platform; print(enterprise_ai_testing_platform.__version__)"
```

---

# Daily Development Workflow

Run while actively developing.

```bash
uv run ruff check . --fix
uv run black .
uv run pytest
```

---

# Before Every Commit

```bash
uv run pre-commit run --all-files
```

---

# Before Every Push or Pull Request

```bash
uv run mypy src
uv run pytest
```

---

# Full Local Quality Gate

Execute before requesting a code review or merging a branch.

```bash
uv run ruff check .
uv run black --check .
uv run mypy src
uv run pytest
```

---

# Updating Dependencies

When dependency versions are intentionally updated:

```bash
uv lock --upgrade
uv sync
```
