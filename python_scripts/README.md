# Python scripts
This is where custom scripts that Airflow can run in dedicated Python containers are stored.

## Files
- `data_import_example.py`: Basic example of a data connector that's used in the `raw_data_import.py` DAG. Connects to a publicly open API and saves the data into our database.
- `Dockerfile`: Used to set up the environment in our dedicated containers spawned with DockerOperator for Python scripts.
- `postgres_utils.py`: Definition of functions that are used to connect to, save in and read from our main Postgres database for dbt.
- `requirements.txt`: Requirements file for the Docker container running our Python scripts.
