.PHONY: help clean clean-pyc clean-build list test test-all coverage docs release sdist

PROJECT_NAME = wine
PYTHON_INTERPRETER = python3

help:
	@echo "clean - remove build artifacts"
	@echo "develop - set up dev environment"
	@echo "install-deps"
	@echo "install-pre-commit"
	@echo "setup-git"
	@echo "lint - check style with flake8"
	@echo "test - run tests quickly with the default Python"
	@echo "run - run train and evaluate model"

clean:
	rm -fr data/
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

setup-git: install-pre-commit
	pre-commit install
	git config branch.autosetuprebase always

install-deps:
	pip install --upgrade pip
	pip install -U pip setuptools wheel
	pip install -r requirements/requirements.txt
	pip install -r requirements/test-requirements.txt

install-pre-commit:
	pip install pre-commit

develop: setup-git install-deps install-pre-commit

lint: install-pre-commit
	@echo "Linting Python files"
	pre-commit run -a
	@echo ""

test: develop lint
	@echo "Running Python tests"
	py.test .
	@echo ""

data: clean
	@echo "Get data from remote"
	$(PYTHON_INTERPRETER)  src/download_data.py

run: data
	@echo "Train and evaluate model"
	$(PYTHON_INTERPRETER) src/main.py
