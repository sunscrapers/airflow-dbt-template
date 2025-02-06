import json
import shlex

from airflow.providers.docker.operators.docker import DockerOperator
from airflow.providers.docker.operators.docker import Mount
from airflow.operators.bash import BashOperator
import os


class OperatorTemplate:

    @staticmethod
    def create_dbt_docker_operator(main_dbt_command, task_id, additional_env_vars=None):
        env_vars = {
            key: val for key, val in dict(os.environ).items() if any([
                key.startswith('DBT_'),
            ])
        }

        all_env_vars_passed_to_container = env_vars | (additional_env_vars if additional_env_vars else {})

        dbt_target = os.getenv('DBT_ENV')
        dbt_logs_host_path = os.getenv('DBT_LOGS_HOST_PATH')
        dbt_main_dir = '/opt/dbt/'
        profiles_dir = '/opt/dbt/config/'
        suffix = f'--target={dbt_target} --profiles-dir={profiles_dir}'

        full_dbt_command = "{main_cmd} {suffix} ".format(
            suffix=suffix,
            target=dbt_target,
            main_cmd=main_dbt_command
        )
        # task_id = task_id + '_docker'

        group = os.getenv('AIRFLOW_GID',0)

        return DockerOperator(
            task_id=task_id,
            user=f'dbt:{group}',
            image='dbt-runner-image',
            container_name='dbt-container-{}'.format(task_id),
            api_version='auto',
            auto_remove=True,
            private_environment=all_env_vars_passed_to_container,
            working_dir=dbt_main_dir,
            command=full_dbt_command,
            mount_tmp_dir=False,
            mounts=[
                Mount(
                    source=dbt_logs_host_path,
                    target='/opt/dbt/logs',
                    type='bind'
                )
            ],
            docker_url="unix://var/run/docker.sock",
            network_mode="host",
            tty=True,
        )


    @staticmethod
    def create_python_script_docker_operator(task_id, command, additional_env_vars=None):
        env_vars = {
            key: val for key, val in dict(os.environ).items() if any([
            ])
        }

        all_env_vars_passed_to_container = env_vars | (additional_env_vars if additional_env_vars else {})

        return DockerOperator(
            task_id=task_id,
            user='airflow',
            image='python-runner-image',
            container_name='python-script-container-{}'.format(task_id),
            api_version='auto',
            auto_remove=True,
            private_environment=all_env_vars_passed_to_container,
            working_dir='/opt/python_scripts/',
            command=command,
            mount_tmp_dir=False,
            docker_url="unix://var/run/docker.sock",
            network_mode="host",
            tty=True
        )
