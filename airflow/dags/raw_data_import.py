from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from dag_templates import DAGTemplate
from operator_templates import OperatorTemplate

with DAGTemplate.create_base_dag(
    dag_id='data_import_example',
    description='Example of data import from XXX',
    schedule_interval='0 4 * * *',
    start_date=datetime(year=2024, month=12, day=3, hour=23),
    tags=['data_import']
) as dag:

    t1 = BashOperator(
        task_id='print_hello',
        bash_command='echo "Hello from test DAG"'
    )

    t2 = OperatorTemplate.create_python_script_docker_operator(
        task_id='data_import_example',
        command="""python3 -c 'print("hello world")'"""
    )
