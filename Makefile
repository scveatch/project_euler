.PHONY: install lint format typecheck all new clean

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
	uv run ruff check . --fix

# Type checking
typecheck:
	uv run mypy .

# Run everything (useful for pre-commit sanity)
all: format lint typecheck 

# Make new problem directory
new: 
	./scripts/new_problem.sh $(NUM) $(TITLE)

# Clean caches
clean:
	rm -rf .pytest_cache .mypy_cache .ruff_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +
