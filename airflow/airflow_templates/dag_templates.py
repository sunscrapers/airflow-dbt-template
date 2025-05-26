import datetime

from airflow import DAG
import os


class DAGTemplate:

    @staticmethod
    def create_base_dag(
            dag_id: str,
            description: str,
            schedule_interval: str,
            start_date,
            catchup=False,
            additional_args=False,
            tags=None,
            concurrency=None,
            max_active_runs=1,
            retries=0,
            params=None
    ):
        app_env = os.environ.get('PYTHON_SCRIPTS_ENVIRONMENT')
        if app_env in ('dev', 'test'):
            schedule_interval = None
        if app_env in ('dev', 'test'):
            start_date = datetime.datetime.now()

        support_email = os.environ.get('AIRFLOW__SUPPORT_EMAIL')
        default_args = {
            'owner': 'airflow',
            'depends_on_past': False,
            'email': [support_email],
            'email_on_failure': False,
            'email_on_retry': False,
            'retries': retries
        }

        additional_args = additional_args if additional_args else {}

        return DAG(
            dag_id,
            default_args={**default_args, **additional_args},
            description=description,
            schedule_interval=schedule_interval,
            start_date=start_date,
            catchup=catchup,
            tags=tags,
            concurrency=concurrency,
            max_active_runs=max_active_runs,
            params=params
        )
