{{
    config(
        materialized='table',
        schema='bronze'
    )
}}

select
    code::varchar(255) as code,
    label::varchar(255) as label
from {{ source('raw_imports', 'eurostat_d3dens_code_label') }}
