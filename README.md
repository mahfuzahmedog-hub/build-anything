# Build Anything

A web app built with AI-supervised development. Every feature verified before marked complete.

## Quick Start

```bash
uv venv
source .venv/bin/activate
uv pip install -e ".[dev]"
uvicorn app.main:app --reload
pytest -q --tb=short
ruff check .
```
