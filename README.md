# Pandas Car Insights

## Summary

- [Pandas Car Insights](#pandas-car-insights)
  - [Summary](#summary)
  - [About the project](#about-the-project)
  - [Getting Started (Quick Local Setup)](#getting-started-quick-local-setup)
    - [1 - Virtual environment](#1---virtual-environment)
    - [2 - Install dependencies](#2---install-dependencies)
    - [3 - Enable imports between modules](#3---enable-imports-between-modules)
    - [4 - Run tests](#4---run-tests)
    - [5 - Test evaluation](#5---test-evaluation)
    - [6 - Code validation](#6---code-validation)
    - [7 - Pre-commit validation](#7---pre-commit-validation)
    - [9 - Most used commands](#9---most-used-commands)
  - [Used technologies](#used-technologies)
  - [Features](#features)

## About the project

Data analysis project with Pandas that cleans car data, organizes it, and produces insights like average MPG per brand.

## Getting Started (Quick Local Setup)

### 1 - Virtual environment

Create a virtual environment to isolate project dependencies

```powershell
python -m venv env
```

Activate the virtual environment

```powershell
.\env\Scripts\activate
```

Activate the virtual environment on Linux or macOS

```bash
source env/bin/activate
```

Deactivate the virtual environment

```powershell
deactivate
```

</br>

### 2 - Install dependencies

Install the project's runtime dependencies

```powershell
pip install -r requirements.txt
```

Update pip if required

```powershell
python -m pip install --upgrade pip
```

Install new packages

```powershell
pip install <nome_da_biblioteca>
```

Save the installed dependencies

```powershell
pip freeze --exclude-editable > requirements.txt
```

### 3 - Enable imports between modules

Make the package importable for local development

```powershell
pip install -e .
```

### 4 - Run tests

Run all tests

```powershell
python -m unittest discover -s tests
```

Run a specific test

```powershell
python -m unittest tests.test_arquivo.TesteClasse.test_funcao
```

### 5 - Test evaluation

Run all tests with coverage

```powershell
coverage run --branch -m unittest discover -s tests
```

Print the result of test execution to the terminal

```powershell
coverage report -m
```

Generate results in JSON

```powershell
coverage json
```

Generate results in XML

```powershell
coverage xml
```

Generate results in HTML

```powershell
coverage html
```

Generate .cover outputs

```powershell
coverage annotate
```

Make sure the tests achieved 100% coverage for the project

```powershell
coverage report --fail-under=100
```

### 6 - Code validation

Check code formatting

```powershell
black --check . --config pyproject.toml
```

Format the code

```powershell
black --config pyproject.toml .
```

Check whether imports are organized

```powershell
isort --check-only --settings-path pyproject.toml .
```

Organize imports

```powershell
isort --settings-path pyproject.toml .
```

Report potential improvements according to PEP8

```powershell
flake8 . --config=.flake8
```

Report potential improvements via Pylint

```powershell
pylint --rcfile=.pylintrc .
```

Analyze potential typing issues

```powershell
mypy --config-file pyproject.toml .
```

Clear MyPy cache (PowerShell)

```powershell
Remove-Item -Recurse -Force ".mypy_cache"
```

Install typing stubs for third-party libraries (used by MyPy)

```powershell
mypy --install-types --non-interactive
```

Analyze potential security issues

```powershell
bandit -r . --configfile pyproject.toml
```

### 7 - Pre-commit validation

Update validation hooks

```powershell
pre-commit autoupdate
```

Clear pre-commit cache

```powershell
pre-commit clean
```

Validate the entire project before committing

```powershell
pre-commit run --all-files
```

Stop pre-commit from running before commits (optional)

```powershell
pre-commit uninstall
```

### 9 - Most used commands

Run all tests with coverage and print the results, listing potential improvements

```powershell
coverage run --branch -m unittest discover -s tests ; coverage report -m
```

Clear MyPy cache (PowerShell) and analyze potential typing issues

```powershell
Remove-Item -Recurse -Force ".mypy_cache" ; mypy --config-file pyproject.toml .
```

Validate project code quality (with tests)

```powershell
pre-commit run --all-files
```

## Used technologies

## Features
