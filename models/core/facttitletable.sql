{{ config(materialized='table') }}

with titleakas as (
    select * from {{ ref('stgtitleakas') }}
), 
titlebasics as (
    select * from {{ ref('stgtitlebasics') }}
),
titleepisode as (
    select * from {{ ref('stgtitleepisode')}}
),
titleratings as (
    select * from {{ ref('stgtitleratings')}}
)

select
    akas.titleId as titleId,
    akas.title as title,
    basics.titleType as titleType,
    basics.primaryTitle as primaryTitle,
    basics.originalTitle as originalTitle,
    basics.startYear as year,
    basics.runtimeMinutes as runtimeMinutes,
    akas.region as region,
    akas.language as language,
    basics.genres as genres,
    episode.parentTconst as parentTitleId,
    episode.seasonNumber as seasonNumber,
    episode.episodeNumber as episodeNumber,
    ratings.averageRating as averageRating,
    ratings.numVotes as numVotes
from titleakas as akas
left outer join titlebasics as basics
on akas.titleId = basics.tconst
left outer join titleepisode as episode
on akas.titleId = episode.tconst
left outer join titleratings as ratings
on akas.titleId = ratings.tconst
