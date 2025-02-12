# DBT Project
This is where the dbt project is defined and set up.

- logs: This is where your dbt logs will be saved. It's a mounted directory so even when the Docker container is restarted or reset, it will be persisted.
- macros: Place for storing defined dbt macros. For now only re-definition of the schema naming macro is saved in order to store tables in explicitly defined schemas within our database.
- models: The main repository for your actual data pipeline. It's split into directories that represent different schemas in the database, in the example it's the medallion architecture with bronze being the raw data models with minimal cleanup and silver is the core data that represents a foundation for the warehouse. The .sql files are used to create new tables/views while the _schema.yml files are there to define the data sources, the model definitions as well as to implement tests for the models.
- seeds: Currently empty, can be used to create static tables in the database with manual inputs.
- snapshots: