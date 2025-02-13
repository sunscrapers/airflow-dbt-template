{% snapshot eurostat_d3dens_code_label_snapshot %}

{{
    config(
        target_schema='snapshot',
        unique_key='code',
        strategy='check',
        check_cols='all',
        invalidate_hard_deletes=True
    )
}}

select
    code,
    label
from {{ ref('eurostat_d3dens_code_label') }}

{% endsnapshot %}
