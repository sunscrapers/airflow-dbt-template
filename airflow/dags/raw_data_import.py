from datetime import datetime
from dag_templates import DAGTemplate
from operator_templates import OperatorTemplate

cmd = 'python3 data_import_example.py'

with DAGTemplate.create_base_dag(
    dag_id='data_import_example',
    description='Example of data import from XXX',
    schedule_interval='0 4 * * *',
    start_date=datetime(year=2025, month=2, day=5, hour=23),
    tags=['data_import']
) as dag:

    t1 = OperatorTemplate.create_python_script_docker_operator(
        task_id='data_import_example',
        command=cmd
    )
