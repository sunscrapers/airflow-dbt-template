# Running Tests

This document explains how to run tests for the Airflow DBT template project.

## Prerequisites

1. Make sure you have Python 3.x installed
2. Install pytest if you haven't already:
   ```bash
   pip install pytest pytest-cov
   ```

## Setup Virtual Environment

Before running tests, it's recommended to set up a virtual environment:

1. Create a virtual environment:
   ```bash
   python -m venv test_venv
   ```

2. Activate the virtual environment:
   - On macOS/Linux:
     ```bash
     source test_venv/bin/activate
     ```
   - On Windows:
     ```bash
     test_venv\Scripts\activate
     ```

3. Install requirements from requirements.txt:
   ```bash
   pip install -r python_scripts/requirements.txt
   ```

4. Install testing dependencies:
   ```bash
   pip install pytest pytest-cov
   ```

## Running All Tests

From the project root directory, run:

```bash
pytest
```

This will discover and run all tests in the project.

## Running with Coverage Report

To run tests with coverage report:

```bash
pytest --cov=dags tests/
```

This generates a coverage report for the DAGs directory.

## Running Specific Tests

To run a specific test file:

```bash
pytest tests/test_project_structure.py
```

To run a specific test function:

```bash
pytest tests/test_project_structure.py::test_dag_files_exist
```

## Verbose Output

For more detailed output:

```bash
pytest -v
```

## Summary

Basic usage:
1. Navigate to project root: `/Users/sunscrapers/Projects/airflow-dbt-template`
2. Run: `pytest`
3. View results in the terminal
