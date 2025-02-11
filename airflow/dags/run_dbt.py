from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from dag_templates import DAGTemplate
from operator_templates import OperatorTemplate

desc = """
    Can be run with additional parameters.
    Example:
    {"dbt_options":"--select your_model_name"}
    or
    {"dbt_run_options":"--select your_model_name --full-refresh"}
    to apply only for dbt run commands
    or together
    {
     "dbt_options":"--select your_model_name",
     "dbt_run_options":" --full-refresh"
    }
"""

with DAGTemplate.create_base_dag(
    dag_id='dbt_example',
    description='Example of dbt pipeline execution',
    schedule_interval='0 2 * * *',
    start_date=datetime(year=2024, month=12, day=3, hour=23),
    tags=['dbt']
) as dag:

    dbt_run_task = OperatorTemplate.create_dbt_docker_operator(
        main_dbt_command='dbt run \
         {{ dag_run.conf["dbt_options"] if "dbt_options" in dag_run.conf else "" }} \
         {{ dag_run.conf["dbt_run_options"] if "dbt_run_options" in dag_run.conf else "" }}',
        task_id='dbt_run_all_t'
    )
    dbt_test_task = OperatorTemplate.create_dbt_docker_operator(
        main_dbt_command='dbt test \
         {{ dag_run.conf["dbt_options"] if "dbt_options" in dag_run.conf else "" }}',
        task_id='dbt_test_all_t'
    )
    dbt_snapshot_task = OperatorTemplate.create_dbt_docker_operator(
        main_dbt_command='dbt snapshot \
         {{ dag_run.conf["dbt_options"] if "dbt_options" in dag_run.conf else "" }}',
        task_id='dbt_snapshot_all_t'
    )

    dbt_run_task >> dbt_test_task >> dbt_snapshot_task
