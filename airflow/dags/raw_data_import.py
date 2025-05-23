from datetime import datetime
from dag_templates import DAGTemplate
from operator_templates import OperatorTemplate

with DAGTemplate.create_base_dag(
    dag_id="data_import_example",
    description="Example of data import from Eurostat API",
    schedule_interval="0 2 * * *",
    start_date=datetime(year=2024, month=12, day=3, hour=23),
    tags=["data_import"],
) as dag:
    t1 = OperatorTemplate.create_python_script_docker_operator(
        task_id="data_import_example", command="""python3 data_import_example.py"""
    )
