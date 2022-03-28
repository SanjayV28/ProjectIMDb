# DTC-Capstone-Project
An End to End Data Engineering Project using GCP,Terraform, Airflow, Docker, DBT!

## Project Description

The objective of the project is to build an end to end data pipeline using the IMDB datasets. To achieve this I have downloaded raw datasets from the IMDB website, uncompressed it, converted it to parquet format and uploaded it to the data lake. Next, Created an External and Partioned/Clustered Tables in the data warehouse for simple analysis on this datasets. Then, Applied transformation and correlated an aggregated table in the data warehouse which will have the complete information about the dataset that can be used for advaanced analysis and also for generating dashboards to the business stackholders.

### Architecture
![image](https://user-images.githubusercontent.com/43469072/160475035-f094861f-0a90-4e21-84ac-844081d9ae7c.png)

### Datasets
This is a subsets of IMDb data are available for access to customers for personal and non-commercial use. Kindly check the below Dataset Location and details.

#### Dataset Location
The dataset files can be accessed and downloaded from https://datasets.imdbws.com/. The data is refreshed daily.

#### Dataset Details
Each dataset is contained in a gzipped, tab-separated-values (TSV) formatted file in the UTF-8 character set. The first line in each file contains headers that describe what is in each column. A ‘\N’ is used to denote that a particular field is missing or null for that title/name. The available datasets are as follows:

**title.akas.tsv.gz** - Contains the following information for titles:
titleId (string) - a tconst, an alphanumeric unique identifier of the title.
ordering (integer) – a number to uniquely identify rows for a given titleId.
title (string) – the localized title.
region (string) - the region for this version of the title.
language (string) - the language of the title.
types (array) - Enumerated set of attributes for this alternative title. 
attributes (array) - Additional terms to describe this alternative title, not enumerated.
isOriginalTitle (boolean) – 0: not original title; 1: original title.

**title.basics.tsv.gz** - Contains the following information for titles:
tconst (string) - alphanumeric unique identifier of the title.
titleType (string) – the type/format of the title (e.g. movie, short, tvseries, tvepisode, video, etc).
primaryTitle (string) – the more popular title / the title used by the filmmakers on promotional materials at the point of release.
originalTitle (string) - original title, in the original language.
isAdult (boolean) - 0: non-adult title; 1: adult title.
startYear (YYYY) – represents the release year of a title. In the case of TV Series, it is the series start year.
endYear (YYYY) – TV Series end year. ‘\N’ for all other title types.
runtimeMinutes – primary runtime of the title, in minutes.
genres (string array) – includes up to three genres associated with the title.

**title.episode.tsv.gz** – Contains the tv episode information. Fields include:
tconst (string) - alphanumeric identifier of episode.
parentTconst (string) - alphanumeric identifier of the parent TV Series.
seasonNumber (integer) – season number the episode belongs to.
episodeNumber (integer) – episode number of the tconst in the TV series.

**title.ratings.tsv.gz** – Contains the IMDb rating and votes information for titles
tconst (string) - alphanumeric unique identifier of the title.
averageRating – weighted average of all the individual user ratings.
numVotes - number of votes the title has received.

Please check out this link https://www.imdb.com/interfaces/ for additional information.

### Technologies
  - Cloud : Google Cloud Platform (GCP)
  - Infrastructure as code (IaC): Terraform
  - Containerization : Docker, Docker Compose
  - Workflow orchestration: Airflow
  - Data Lake: Google Cloud Storage (GCS)
  - Data Wareshouse:  Google BigQuery
  - Transformation: Data Build Tool (DBT)
  - Visualization: Google Data Studio
