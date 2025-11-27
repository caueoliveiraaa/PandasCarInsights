# Pandas Car Insights

Data analysis project with Pandas that cleans car data, organizes it, and produces insights like average MPG per brand.

## Summary

- [Pandas Car Insights](#pandas-car-insights)
  - [Summary](#summary)
  - [Folder and File Structure](#folder-and-file-structure)
  - [Getting Started (Quick Local Setup)](#getting-started-quick-local-setup)
    - [1 - Virtual environment](#1---virtual-environment)
    - [2 - Install dependencies](#2---install-dependencies)
    - [3 - Enable imports between modules](#3---enable-imports-between-modules)
    - [4 - Run tests](#4---run-tests)
    - [5 - Test evaluation](#5---test-evaluation)
    - [6 - Code validation](#6---code-validation)
    - [7 - Pre-commit validation](#7---pre-commit-validation)
    - [9 - Most used commands](#9---most-used-commands)

## Folder and File Structure

This section describes the current structure of the repository and purpose of each folder/file.

- `.github/workflows` - Contains continuous integration (CI) configuration. Currently includes `integracao_continua.yml` (CI/validation pipeline).
- `.vscode` - VS Code configuration files (for example, `settings.json` and `launch.json`). These contain editor and debug settings that work well with the project's formatters and linters.
- `database/` - Contains sample dataset(s). Example: `data_set.json` (raw JSON dataset used in notes and scripts).
- `scripts/` - Folder for scripts, helpers or automation; currently empty (may host ETL or analysis scripts).
- `out/` - Output folder used to store results (e.g. CSV files produced after cleaning/analysis).
- `tests/` - Unit/integration tests. Use `unittest` discovery to run these.
- `main.py` - Project entrypoint (currently empty).
- `notes.txt` - Project notes describing the intended data cleaning and analysis steps.
- `pyproject.toml` - Configuration for development tools (Black, isort, Mypy, Coverage, Bandit and others).
- `setup.py` - Project installation script. It reads `requirements.txt` to build `install_requires` for setuptools.
- `requirements.txt` - NOT present in the repository yet but expected by `setup.py` and by the CI workflow; add a `requirements.txt` with runtime dependencies before using CI or building the package.
- `.flake8`, `.pylintrc`, `.pre-commit-config.yaml` - Quality & linter configuration files.

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
