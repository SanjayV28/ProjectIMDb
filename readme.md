# ProjectIMDb
An End to End Data Engineering Project using the IMdb datasets and by utilising the tools like Google Cloud Platform(GCP),Terraform, Airflow, Docker,and DBT!

## Project Description

### Problem Statement

The Internet Movie Database (IMDb) is the world's most popular and the latgest authoritative source for movie, TV and celebrity content, designed to help fans explore the world of movies and shows. But the challenging part about the IMDb data is they are divided and stored into multiple files in which each file will have only the certain amount of information.

### Solution

To address the above problem, We are building this project solution using the best practices of Data Engineering. Our objective is to have one final desired table which will have an entire information and make it available for both advanced analytics and visualisations by following the below steps!

- Configure the Project Infrastructure using **Terraform**. Please check out the instructions [here](https://github.com/SanjayV28/ProjectIMDb/blob/74b124e6053cc58b4b22fc36df9c0c6198ae7ae7/terraform/readme.md).
- Create a data pipeline using **Airflow** for processing the dataset, uploading it to the datalake, moving the data from the data lake to a data warehouse and create an external and partioned/clustered tables. Please check out the instructions [here](https://github.com/SanjayV28/ProjectIMDb/blob/74b124e6053cc58b4b22fc36df9c0c6198ae7ae7/airflow/readme.md).
- Transform the data in the data warehouse using **Data Build Tool(DBT)** and prepare it for analytics and visualisations. Please check out the instructions [here](https://github.com/SanjayV28/ProjectIMDb/blob/74b124e6053cc58b4b22fc36df9c0c6198ae7ae7/dbt/readme.md).
- Created a dashboard using **Google Data Studio**. Please check out the instructions [here](https://github.com/SanjayV28/ProjectIMDb/blob/74b124e6053cc58b4b22fc36df9c0c6198ae7ae7/datastudio/readme.md).

### Architecture
![ProjectArchitecture](https://github.com/SanjayV28/ProjectIMDb/blob/466a70161f63050e0ef1d3f6c3b336b0550bd577/images/ProjectArchitecture.png)

### Dataset
This is a subsets of IMDb data are available for access to customers for personal and non-commercial use. The data is refreshed daily. The dataset files can be accessed and downloaded [here](https://datasets.imdbws.com/.)

#### Dataset Details
Each dataset is contained in a gzipped, tab-separated-values (TSV) formatted file in the UTF-8 character set. The first line in each file contains headers that describe what is in each column. A ‘\N’ is used to denote that a particular field is missing or null for that title/name. The available datasets are as follows:

- **title.akas.tsv.gz** - This dataset contains the following information for titles: titleId, ordering, title, region, language, types, attributes, and isOriginalTitle.
- **title.basics.tsv.gz** - This dataset contains the following information for titles: tconst, titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes, and genres.
- **title.episode.tsv.gz** – This dataset contains the following information for tv episode: tconst, parentTconst, seasonNumber, and episodeNumber.
- **title.ratings.tsv.gz** – This dataset contains the information about the IMDb rating and votes information for titles: tconst, averageRating, and numVotes.

Please check out this link [here](https://www.imdb.com/interfaces/) for additional information.

### Technologies
  - Cloud : **Google Cloud Platform (GCP)**
  - Infrastructure as code (IaC): **Terraform**
  - Containerization : **Docker, Docker Compose**
  - Workflow orchestration: **Airflow**
  - Data Lake: **Google Cloud Storage (GCS)**
  - Data Wareshouse:  **Google BigQuery**
  - Transformation: **Data Build Tool (DBT)**
  - Visualisation: **Google Data Studio**

### Final Dashboard

![Dashbaord](https://github.com/SanjayV28/ProjectIMDb/blob/74b124e6053cc58b4b22fc36df9c0c6198ae7ae7/images/Dashboard.png)

### Project Prerequisites

...

### Next steps

...
