PYTHON_DEV_CONTAINER_NAME := python-script-image
AIRFLOW_DOCKER_COMPOSE_FILE := docker-compose.yaml
AIRFLOW_POSTRGRES_VOLUME_NAME := airflow-dbt-template_postgres-db-volume
POSTGRES_DBT_VOLUME_NAME := postgres-dbt-data

start_all:
	docker compose up -d

stop_all:
	docker compose down

restart_all:
	docker compose down
	docker compose up -d

recreate_all:
	docker compose down
	docker builder prune -f
	docker compose build --progress=plain --no-cache
	docker compose up -d

recreate_all_clean_db:
	docker compose down
	@if docker volume ls -q | grep -q "^${AIRFLOW_POSTRGRES_VOLUME_NAME}$$"; then \
		docker volume rm ${AIRFLOW_POSTRGRES_VOLUME_NAME}; \
	fi
	@if docker volume ls -q | grep -q "^${POSTGRES_DBT_VOLUME_NAME}$$"; then \
		docker volume rm ${POSTGRES_DBT_VOLUME_NAME}; \
	fi
	docker builder prune -f
	docker compose build --progress=plain --no-cache
	docker compose up -d

run_tests:
	python -m venv test_venv && \
	source test_venv/bin/activate && \
	pip install -r python_scripts/requirements.txt && \
	pip install -r tests/test-requirements.txt && \
	pip install pytest pytest-cov && \
	pytest --cov=dags tests/ -v && \
	deactivate && \
	rm -rf test_venv