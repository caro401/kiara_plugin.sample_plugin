.PHONY: clean clean-test clean-pyc clean-build docs help
.DEFAULT_GOAL := help

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache
	rm -fr .mypy_cache

init: clean ## initialize a development environment (to be run in virtualenv)
	git init
	pip install -U pip
	pip install -U -e '.[dev_utils,dev_testing]'
	pre-commit install
	pre-commit install --hook-type commit-msg
	git add "*" ".*"
	pre-commit run --all-files || true
	git add "*" ".*"

update-dependencies:  ## update all development dependencies
	pip install -U pip
	pip install -U -e '.[dev_utils,dev_testing]'

typecheck: ## run mypy
	mypy --config-file pyproject.toml --ignore-missing-imports "src/"

test: ## run tests quickly with the default Python
	pytest

coverage: ## check code coverage quickly with the default Python
	coverage run -m pytest tests
	coverage html --skip-covered --skip-empty
	coverage report

check: pre-commit typecheck test

pre-commit: ## run pre-commit on all files
	pre-commit run --all-files

dist: clean ## build source and wheel packages
	python -m build
	ls -l dist

gen-docs-data:
	kiara info plugin explain kiara_plugin.sample_plugin --format json > ./docs/src/content/plugin_data/kiara_plugin.sample_plugin-v${TAG}.json

build-docs: gen-docs-data
	cd docs && npm run build

serve-docs:
	cd docs && npm run dev
