{% snapshot eurostat_d3dens_id_code_snapshot %}

{{
    config(
        target_schema='snapshot',
        unique_key='id',
        strategy='check',
        check_cols='all',
        invalidate_hard_deletes=True
    )
}}

select
    id,
    code
from {{ ref('eurostat_d3dens_id_code') }}

{% endsnapshot %}
