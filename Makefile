SHELL:=/usr/bin/env bash

.PHONY: lint
lint:
	poetry run mypy generic_args tests
	poetry run flakehell lint generic_args tests

.PHONY: unit
unit:
	poetry run pytest

.PHONY: package
package:
	poetry check
	poetry run pip check
	poetry run safety check --full-report

.PHONY: test
test: lint package unit

.PHONY: format
format:
	poetry run isort generic_args tests
