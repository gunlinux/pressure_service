.PHONY: check lint format type-check lock tests

check: lint format type-check lock

lint:
	uvx ruff check .

format:
	uvx ruff format --check .

tests:
	uv run pytest --cov=app

type-check:
	uv run pyright .

lock:
	uv lock --locked

dev:
	uv run uvicorn app.main:app --reload

