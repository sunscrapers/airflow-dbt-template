FROM apache/airflow:2.10.4-python3.11

ENV TZ="Europe/Warsaw"

USER root
RUN apt-get update && apt-get -y install gcc && apt-get clean

# Create directories first
RUN mkdir -p /opt/airflow/dags /opt/airflow/config /opt/airflow/airflow_templates /opt/python_scripts /opt/dbt/{target,manifest_freeze}

# Copy files
COPY ./airflow/dags /opt/airflow/dags/
COPY ./airflow/config /opt/airflow/config/
COPY ./airflow/airflow_templates /opt/airflow/airflow_templates/
COPY ./python_scripts /opt/python_scripts/

# Set permissions explicitly
RUN chown -R airflow:root /opt/airflow /opt/python_scripts /opt/dbt && \
    chmod -R 755 /opt/airflow/dags && \
    chmod -R 755 /opt/airflow/airflow_templates && \
    chmod -R 755 /opt/python_scripts && \
    chmod -R g+w /opt/dbt/{target,manifest_freeze}

ENV PYTHONPATH "${PYTHONPATH}:/opt/airflow/airflow_templates/"

RUN groupadd -g 999 docker && \
    usermod -aG docker airflow

USER airflow
