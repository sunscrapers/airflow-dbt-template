FROM apache/airflow:2.10.4-python3.11

ENV TZ="Europe/Warsaw"

USER root
RUN apt-get update && apt-get -y install gcc && apt-get clean

COPY ./airflow/dags /opt/airflow/dags/
COPY ./airflow/config /opt/airflow/config/
COPY ./airflow/airflow_templates /opt/airflow/airflow_templates/
COPY ./python_scripts /opt/python_scripts/

RUN chown -R airflow: /opt/{airflow,python_scripts} && mkdir -p /opt/dbt/{target,manifest_freeze} && chmod -R g+w /opt/dbt/{target,manifest_freeze}

# Place for the custom python scripts which will be imported by DAGs
ENV PYTHONPATH "$PYTHONPATH:/opt/airflow/airflow_templates/"
RUN mkdir -p /opt/airflow/airflow_templates/ && chmod -R +x /opt/airflow/airflow_templates/

USER airflow
