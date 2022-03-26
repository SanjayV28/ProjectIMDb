{{ config(materialized='view') }}

with basics as(
    select 
        tconst,
        titleType,
        primaryTitle,
        originalTitle,
        isAdult,
        replace(startYear, "\\N", "0") as startYear,
        replace(endYear, "\\N", "0") as endYear,
        replace(runtimeMinutes, "\\N", "0") as runtimeMinutes,
        genres
    from {{ source('raw','externaltitlebasics') }}
)
select 
    cast(tconst as string) as tconst,
    cast(titleType as string) as titleType,
    cast(primaryTitle as string) as primaryTitle,
    cast(originalTitle as string) as  originalTitle,
    cast(isAdult as integer) as isAdult,
    cast(startYear as integer) as startYear,
    cast(endYear as integer) as endYear,
    cast(runtimeMinutes as integer) as runtimeMinutes,
    cast(genres as string)as genres
from basics
