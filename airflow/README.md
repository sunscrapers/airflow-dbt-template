This is where all Airflow files are located

Directories:
- airflow_templates: Helper classes definition that allow for quicker and easier definition of DAGs and operators within the DAG files
- config: For now an empty directory for future Airflow config files
- dags: Main directory where Airflow DAGs are configurated. These DAGs mainly rely on the operator and DAG templates from airflow_templates. You can see two example implementations there: one for a Python connector that pulls data from an API and puts it in your database, another for a DAG that runs full dbt data processing pipeline, including tests and snapshots.
- logs: Directory in which your Airflow logs will be saved
- plugins: For now an empty directory for future Airflow plugin files