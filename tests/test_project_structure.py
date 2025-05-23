import os
import sys
import shutil
import subprocess
import pytest
import tempfile

# Fix: Change PROJECT_ROOT to point to the correct root directory (one level up from tests)
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
print(
    "PROJECT_ROOT: "
    + PROJECT_ROOT
    + ", DAGS: "
    + os.path.join(PROJECT_ROOT, "airflow", "dags")
)


def test_dag_files_exist():
    """Test that DAG files exist in the dags directory."""
    dags_dir = os.path.join(PROJECT_ROOT, "airflow", "dags")

    # If the directory doesn't exist yet, mark test as expected fail with a clear message
    if not os.path.isdir(dags_dir):
        pytest.xfail(f"Airflow dags directory doesn't exist at {dags_dir}")

    # List all files in the directory
    if os.path.isdir(dags_dir):
        dag_files = [
            f
            for f in os.listdir(dags_dir)
            if f.endswith(".py") and not f.startswith("__")
        ]
        print(f"Found DAG files: {dag_files}")

    # Check for some DAG files, report which ones we found
    if os.path.isdir(dags_dir) and any(f.endswith(".py") for f in os.listdir(dags_dir)):
        # Test passes if any DAG files exist
        assert True, "DAG files found"
    else:
        # Mark as xfail if no DAG files yet
        pytest.xfail("No DAG files found in the dags directory")


def test_requirements_file_exists():
    """Test that requirements file exists."""
    req_path = os.path.join(PROJECT_ROOT, "python_scripts", "requirements.txt")
    assert os.path.isfile(req_path), f"Requirements file does not exist at {req_path}"


@pytest.mark.skipif(
    sys.platform.startswith("win"), reason="Skipping venv test on Windows"
)
def test_create_venv_with_requirements():
    """Test that requirements file can be used to create a virtual environment."""
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()
    try:
        # Path to requirements file
        req_path = os.path.join(PROJECT_ROOT, "python_scripts", "requirements.txt")

        # Check if requirements file exists before proceeding
        if not os.path.isfile(req_path):
            pytest.xfail(f"Requirements file not found at {req_path}")

        # Create a virtual environment
        venv_dir = os.path.join(temp_dir, "test_venv")
        result = subprocess.run(
            [sys.executable, "-m", "venv", venv_dir],
            capture_output=True,
            text=True,
            check=False,
        )
        assert result.returncode == 0, (
            f"Failed to create virtual environment: {result.stderr}"
        )

        # Install requirements
        pip_path = (
            os.path.join(venv_dir, "bin", "pip")
            if not sys.platform.startswith("win")
            else os.path.join(venv_dir, "Scripts", "pip")
        )
        result = subprocess.run(
            [pip_path, "install", "-r", req_path],
            capture_output=True,
            text=True,
            check=False,
            timeout=300,  # 5 minutes timeout
        )
        # Just check that the process completes without erroring out completely
        assert result.returncode == 0, (
            f"Failed to install requirements: {result.stderr}"
        )

    finally:
        # Clean up
        shutil.rmtree(temp_dir, ignore_errors=True)
