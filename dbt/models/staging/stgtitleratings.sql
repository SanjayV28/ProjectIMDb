{{ config(materialized='view') }}

with ratings as(
    select
       tconst,
       averageRating,
       numVotes
    from {{ source('raw','externaltitleratings') }}
)
select 
    cast(tconst as string) as tconst,
    cast(averageRating as numeric) as averageRating,
    cast(numVotes as integer) as numVotes
from ratings