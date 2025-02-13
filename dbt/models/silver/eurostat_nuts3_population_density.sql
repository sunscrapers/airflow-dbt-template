
{{ 
    config(
        materialized='table',
        schema='silver'
    ) 
}}

select
    eurostat_d3dens_id_value.id,
    eurostat_d3dens_id_code.code,
    eurostat_d3dens_code_label.label,
    eurostat_d3dens_id_status.status,
    eurostat_d3dens_id_value.value
from {{ ref('eurostat_d3dens_id_value') }}
join {{ ref('eurostat_d3dens_id_status') }}
    on eurostat_d3dens_id_value.id = eurostat_d3dens_id_status.id
join {{ ref('eurostat_d3dens_id_code') }}
    on eurostat_d3dens_id_value.id = eurostat_d3dens_id_code.id
join {{ ref('eurostat_d3dens_code_label') }}
    on eurostat_d3dens_id_code.code = eurostat_d3dens_code_label.code
