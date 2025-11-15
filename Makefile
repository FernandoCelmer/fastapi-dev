.PHONY: lint format format-check type-check check-all fix

# Code Quality commands using .code_quality config files
# Alternative: use scripts/code-quality.sh directly

lint:
	@poetry run flake8 --append-config=.code_quality/.flake8 .
	@poetry run ruff check --config=.code_quality/ruff.toml .

format:
	@poetry run black .
	@poetry run isort .

format-check:
	@poetry run black --check .
	@poetry run isort --check-only .

type-check:
	@poetry run mypy --config-file=.code_quality/mypy.ini .

check-all: lint format-check type-check

fix: format lint

