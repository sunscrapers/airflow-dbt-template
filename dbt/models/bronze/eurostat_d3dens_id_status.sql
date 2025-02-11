{{
    config(
        materialized='table',
        schema='bronze'
    )
}}

select
    id::int as id,
    status::varchar(255) as status
from {{ source('raw_imports', 'eurostat_d3dens_id_status') }}
