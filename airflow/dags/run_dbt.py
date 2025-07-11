from datetime import datetime
from airflow.models.param import Param
from dag_templates import DAGTemplate
from operator_templates import OperatorTemplate

with DAGTemplate.create_base_dag(
    dag_id="dbt_example",
    description="Example of dbt pipeline execution",
    params={
        "dbt_options": Param(
            default=" ",
            type=["string", "null"],
            description="Pass on any dbt arguments such as '--select model_name'",
        )
    },
    schedule_interval="0 4 * * *",
    start_date=datetime(year=2024, month=12, day=3, hour=23),
    tags=["dbt"],
) as dag:
    dbt_run_task = OperatorTemplate.create_dbt_docker_operator(
        main_dbt_command='dbt run {{ dag_run.conf.get("dbt_options") or " " }}',
        task_id="dbt_run_all_t",
    )
    dbt_test_task = OperatorTemplate.create_dbt_docker_operator(
        main_dbt_command='dbt test {{ dag_run.conf.get("dbt_options") or " " }}',
        task_id="dbt_test_all_t",
    )
    dbt_snapshot_task = OperatorTemplate.create_dbt_docker_operator(
        main_dbt_command='dbt snapshot {{ dag_run.conf.get("dbt_options") or " " }}',
        task_id="dbt_snapshot_all_t",
    )

    dbt_run_task >> dbt_test_task >> dbt_snapshot_task
