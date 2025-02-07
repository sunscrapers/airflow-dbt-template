PYTHON_DEV_CONTAINER_NAME := python-script-image
AIRFLOW_DOCKER_COMPOSE_FILE := docker-compose.yaml
AIRFLOW_POSTRGRES_VOLUME_NAME := airflow-dbt-template_postgres-db-volume

recreate_all:
	docker compose down
	@if docker volume ls -q | grep -q "^${AIRFLOW_POSTRGRES_VOLUME_NAME}$$"; then \
        docker volume rm ${AIRFLOW_POSTRGRES_VOLUME_NAME}; \
    else \
        echo "Volume ${AIRFLOW_POSTRGRES_VOLUME_NAME} does not exist"; \
    fi
	docker builder prune -f
	docker compose build --progress=plain --no-cache
	docker compose up -d

restart_all:
	docker compose down
	docker compose up -d
