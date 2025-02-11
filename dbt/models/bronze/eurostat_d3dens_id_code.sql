{{
    config(
        materialized='table',
        schema='bronze'
    )
}}

select
    id::int as id,
    code::varchar(255) as code
from {{ source('raw_imports', 'eurostat_d3dens_id_code') }}