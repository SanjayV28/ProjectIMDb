{{ config(materialized='view') }}

with episode as(
    select 
        tconst,
        parentTconst,
        replace(seasonNumber, "\\N", "0") as seasonNumber,
        replace(episodeNumber, "\\N", "0") as episodeNumber,
    from {{ source('raw','externaltitleepisode') }}
)
select 
    cast(tconst as string) as tconst,
    cast(parentTconst as string) as parentTconst,
    cast(seasonNumber as integer) as seasonNumber,
    cast(episodeNumber as integer) as  episodeNumber
from episode