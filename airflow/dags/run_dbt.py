from datetime import datetime
from dag_templates import DAGTemplate
from operator_templates import OperatorTemplate

desc = """
    Can be run with additional parameters.
    Example:
    {"dbt_options":"--select staging_phone_call"}
    or
    {"dbt_run_options":"--select staging_phone_call --full-refresh"}
    to apply only for dbt run commands
    or together
    {
     "dbt_options":"--select staging_phone_call",
     "dbt_run_options":" --full-refresh"
    }
"""

with DAGTemplate.create_base_dag(
    dag_id='dbt_daily',
    description='Daily run of full dbt workflow (no imports)',
    schedule_interval='0 2 * * *',
    start_date=datetime(year=2024, month=12, day=3, hour=23),
    tags=['dbt']
) as dag:

    dbt_seed_task = OperatorTemplate.create_dbt_docker_operator(
        main_dbt_command='dbt seed --full-refresh --exclude tag:excluded_from_main_flow \
         {{ dag_run.conf["dbt_options"] if "dbt_options" in dag_run.conf else "" }}',
        task_id='dbt_seed_all_t'
    )
    dbt_run_task = OperatorTemplate.create_dbt_docker_operator(
        main_dbt_command='dbt run --exclude tag:after_snapshot tag:excluded_from_main_flow \
         {{ dag_run.conf["dbt_options"] if "dbt_options" in dag_run.conf else "" }} \
         {{ dag_run.conf["dbt_run_options"] if "dbt_run_options" in dag_run.conf else "" }}',
        task_id='dbt_run_all_t'
    )
    dbt_test_task = OperatorTemplate.create_dbt_docker_operator(
        main_dbt_command='dbt test -s tag:for_snapshot --exclude tag:after_snapshot tag:excluded_from_main_flow \
         {{ dag_run.conf["dbt_options"] if "dbt_options" in dag_run.conf else "" }}',
        task_id='dbt_test_all_t'
    )
    dbt_snapshot_task = OperatorTemplate.create_dbt_docker_operator(
        main_dbt_command='dbt snapshot --exclude tag:excluded_from_main_flow \
         {{ dag_run.conf["dbt_options"] if "dbt_options" in dag_run.conf else "" }}',
        task_id='dbt_snapshot_all_t'
    )
    dbt_run_after_snapshot_task = OperatorTemplate.create_dbt_docker_operator(
        main_dbt_command='dbt run --select tag:after_snapshot --exclude tag:excluded_from_main_flow  \
         {{ dag_run.conf["dbt_options"] if "dbt_options" in dag_run.conf else "" }} \
         {{ dag_run.conf["dbt_run_options"] if "dbt_run_options" in dag_run.conf else "" }}',
        task_id='dbt_run_after_snapshot_t'
    )
    dbt_test_after_snapshot_task = OperatorTemplate.create_dbt_docker_operator(
        main_dbt_command='dbt test --exclude tag:excluded_from_main_flow \
         {{ dag_run.conf["dbt_options"] if "dbt_options" in dag_run.conf else "" }}',
        task_id='dbt_test_after_snapshot_t'
    )

    dbt_seed_task >> dbt_run_task >> dbt_test_task >> dbt_snapshot_task >> \
    dbt_run_after_snapshot_task >> dbt_test_after_snapshot_task
