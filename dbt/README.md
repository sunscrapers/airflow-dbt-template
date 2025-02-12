# DBT Project
This is where the dbt project is defined and set up.

## Directories
- `logs/`: This is where your dbt logs will be saved. It's a mounted directory so even when the Docker container is restarted or reset, it will be persisted.
- `macros/`: Place for storing dbt macros. For now, it includes a custom schema naming macro to place tables in the correct schemas.
- `models/`: The main repository for your actual data pipeline. The subdirectories (e.g., `bronze`, `silver`) represent different layered schemas. SQL files create tables/views, while `_schema.yml` files define data sources, model metadata, and tests.
- `seeds/`: (Currently empty) Used for creating static tables from CSV or similar.
- `snapshots/`: Where you define snapshots to track historical changes in data tables.
- `target/`: This is where dbt stores compiled queries and artifacts. It's a mounted directory, so files persist across container restarts.

## Setup files
- `dbt_project.yml`: The main configuration file for dbt. It defines folder paths, naming conventions, profiles, and other project-wide settings.
- `Dockerfile`: File that is used to set up the dedicated dbt container for our DAG DockerOperator. Creates the environment in which dbt runs.
- `packages.yml`: Defines the dbt packages we want to have installed. We've got dbt-utils there that we'll use for testing our models.
- `profiles.yml-template`: Template file that you should fill in and rename to `profiles.yml` before running your project.
- `requirements.txt`: File with required Python packages that we'll need in our Docker environment
