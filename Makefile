.PHONY: install lint format typecheck all clean

# Install environment
install:
	uv sync

# Run linting
lint:
	uv run ruff check .
	uv run codespell . 

# Auto-format code
format:
	uv run ruff format .

# Type checking
typecheck:
	uv run mypy .

# Run everything (useful for pre-commit sanity)
all: format lint typecheck 

# Clean caches
clean:
	rm -rf .pytest_cache .mypy_cache .ruff_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +
