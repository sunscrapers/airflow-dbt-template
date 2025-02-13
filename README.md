# Airflow + dbt template
This repository is a template for starting your data pipeline and orchestration with Airflow and dbt at its core.
The idea is to build it step-by-step so there are core branches called `part-X-` that will guide you from a simple, local setup in Docker to a more complex implementation deployed in the cloud with CI/CD.
You can follow the full description of the project in our blog posts here **(add link)**.

## Prerequisites
- [Docker](https://www.docker.com/): we'll be running all of our code in Docker containers, so make sure you have Docker installed and running on your machine
- [Python](https://www.python.org/): both Airflow and dbt are based on Python and all our custom scripts will also be primarily Python, so for local testing and prototyping ensure you have Python installed. Most of the actual execution will happen in Docker though, so your local machine environment will not directly impact it.

## How does it work
The general idea for this template is to simplify the setup as much as possible in order to let you focus on the actual work of a data engineer - building the data connectors and pipelines and maintaining a clean a reliable datasource for your users. To achieve this, we prepared a set of pre-configured files that you'll  only have to adjust slightly to get your project running locally.

### Initial setup
The files that you'll have to edit before you can start the project locally are the following:
- `.env-template`: Take this file and save it in the same directory under `.env` name. Make changes to the usernames, passwords and variable names as you please. This will be used across the project to set it up according to your preference. Once we move on to deploying the project in production environments, we'll have different versions of these files (or even different ways to manage environmental variables) per each env.
- `dbt/profiles.yml-template`: Similarly, take this file and save it to the `dbt/profiles.yml` file. In our default setup it's pulling from `.env`, but you can change it if you prefer.

### Launching the template locally
Once you're done with the initial setup, you can launch the project using our pre-defined commands stored in `Makefile`:
- `make build_all`: This command will first build your Docker images and then start the containers with services
- `make start_all`: If the images are already built, but containers are not running it will start them.
- `make stop_all`: Stops the running containers.
- `make restart_all`: Combines the `start_all` and `stop_all` commands.
- `make recreate_all`: This command stops all containers, deletes all the images and cache and then re-builds images and restarts the containers. It'll provide a verbose output to improve debugging.
- `make recreate_all_clean_db`: Same as `recreate_all`, but also deletes the volumes that are mounted in Docker. This means that both the Airflow database that stores metadata for Airflow and the Postgres database we're using for our dbt project will be fully deleted and created from scratch.

When you first set up you project, you can run `make build_all` and you see that:
- Airflow web UI should be availabe in your browser, by default at `localhost:8080`
- The dbt Postgres database will be available for you to connect to, by default at `localhost:5435`

Once you run the DAGs in Airflow (first import the data with `data_import_example`, then process it with `dbt_example`), you can review the data in Postgres by connecting to it locally.

## Directories
- `airflow/`: This is where Airflow DAGs are, as well as some template helper Python scripts, Airflow logs and configs
- `dbt/`: Repository for the dbt models, schema definitions and config files
- `python_scripts/`: Place to store Python scripts that we'll use in our data pipeline. It's also where the environment for those scripts is defined in the `Dockerfile` and `requirements.txt`

## Setup files
- `docker-compose.yml`: Single Docker compose file for all of the Docker images used in the project - Airflow orchestration, Postgres databases as well as Docker operators for dbt and Python used in DAGs.
- `Dockerfile`: Dockerfile for Airflow container.
- `Makefile`: We store our `make` commands here to streamline the management experience of the project.
