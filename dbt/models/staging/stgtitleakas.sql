{{ config(materialized='view') }}

with akas as(
    select 
        titleId,
        ordering,
        title,
        region,
        replace(language, "\\N", "") as language,
        types,
        attributes,
        isOriginalTitle
    from {{ source('raw','externaltitleakas') }}
)
select 
    cast(titleId as string) as titleId,
    cast(ordering as integer) as ordering,
    cast(title as string) as title,
    cast(region as string) as  region,
    cast(language as string) as language,
    cast(types as string) as types,
    cast(attributes as string) as attributes,
    cast(isOriginalTitle as integer) as isOriginalTitle
from akas
