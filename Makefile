.PHONY: help clean lint fmt mt-check test pre-commit

help:
	@echo ""
	@echo "Use 'make <command>'"
	@echo ""
	@echo "commands"
	@echo "  venv				create venv and install dependencies"
	@echo "  clean				remove cleanable files"
	@echo "  lint				run linters"
	@echo "  fmt				run formaters"
	@echo "  fmt-check			run formatting check"
	@echo "  test				run all tests"
	@echo "  pre-commit			run pre-commit standardization"
	@echo ""
	@echo "Check the Makefile to know exactly what each target is doing."

venv:
	@python -m venv venv

	@poetry install \
		&& poetry run pre-commit install \
		&& poetry run maturin develop

clean:
	-@rm -rf venv
	-@rm -fr `find . -name __pycache__`
	-@rm -rf .pytest_cache
	-@rm -rf .mypy_cache
	-@rm -rf target

lint: venv
	@poetry run flake8 \
		pylamine \
		tests
	@cargo clippy

fmt: venv
	@poetry run isort . \
		&& poetry run black .
	@cargo fmt

fmt-check: venv
	@poetry run isort . --check \
		&& poetry run black . --check
	@cargo fmt --check

test: venv
	@poetry run pytest

pre-commit: test fmt lint
	@poetry run mypy \
		pylamine \
		tests
