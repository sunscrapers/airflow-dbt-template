{{
    config(
        materialized='table',
        schema='bronze'
    )
}}

select
    id::int as id,
    value::float8 as value
from {{ source('raw_imports', 'eurostat_d3dens_id_value') }}
