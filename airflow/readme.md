# Data Pipeline Orchestration

There are plenty of workflow orchestration tools (like Airflow, Prefect, Luigi) available to set up our data pipelines. I have used **Apache Airflow** to set up the data pipeline for this project. In **Airflow**, we can define DAGs in python to set up our data pipelines. 

## Installation
Installing Airflow is quite challenging, the best practice is to install it with Docker. Please make sure that you have installed Docker and Docker Compose (Refer project prerequisites) and follow the instructions mentioned [here](https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html) for installing airflow.

## Running Airflow with Docker
Now we have successfully completed the Docker setup. We can start with our data pipeline by following the below steps.

- In the cloned repository, Navigate to the airflow directory.
  ```
  cd airflow
  ```
- Setting up the user ID and necessary folders for airflow.
  > **Note:** Make sure you are running the below commands in your IDE terminal
  ```
  mkdir -p ./dags ./logs ./plugins
  echo -e "AIRFLOW_UID=$(id -u)" > .env
  ```
- To Standardize the credentials, rename the service account json file as `google_credentials.json` and move it to `~/.google/credentials/` folder in your home directory.
- Set the environment variables for the below GCP resources in your Docker file.
  - GCP Project ID = **Project-ID**
  - Google Cloud Storage Bucket Name = **Bucket-Name**
  - GCP BigQuery Dataset Name = **Dataset-Name**
- Start the airflow by building the image (only first-time, or when there's any change in the Dockerfile, takes ~15 mins for the first-time)
  ```
  docker-compose build
  ```
- When you have successfully built the image, kick-start all the related services from the container
  ```
  docker-compose up
  ```
- In another terminal, run `docker-compose ps` to see which containers are up & running healthy.
- Now we have successfully completed the Airflow setup. Login to Airflow web UI on `localhost:8080` with the default credentials.
  - Username: **airflow**
  - Password: **airflow**
  
 - Trigger/Run your DAGs on the Web Console.
 - Once your pipelines are completed successfully, shut down the containers.
    ```
    docker-compose down
    ```
 ## DAGs
 
 - For this project, We will set up four DAGs called `titleakas_dag.py`, `titlebasics_dag.py`, `titleepisode_dag.py` and `titleratings_dag.py`.
 - These DAGs are scheduled to run on a daily basis because the data source IMDb is refreshed daily.
 - These DAGs are similar in structure and have multiple tasks.
 - DAGs Flow:
 
   ![DAGs flow](https://github.com/SanjayV28/ProjectIMDb/blob/4355dd5a23e059a1032d678799ddc771370abad9/images/DAGsGraph.png)
   
   - The above tasks shown are same in all the four dags `titleakas_dag.py`, `titlebasics_dag.py`, `titleepisode_dag.py` and `titleratings_dag.py`.
   - These DAGs will download the raw dataset from the IMDb Website and uncompress it. 
   - Convert the uncompressed datasets to parquet format.
   - Upload the converted parquet file into Google Cloud Storage Bucket. 
   - Create an external tables from the parquet files uploaded in GCS Bucket.
     - externalttitleakas - external table for titleakas
     - externalttitlebasics - external table for titlebasics
     - externalttitleepisode - external table for titleepisode
     - externalttitleratings - external table for titleratings
   - Create a partitioned/clustered tables from the external tables.
     >**Note:** My query patterns are based on categorical columns(mostly of string datatype). So I have used only clustering to optimize my tables.
     - titleakas - This is a clustered table created from `externalttitleakas` and clustered by `titleid`,`region`,and `language`
     - titlebasics - This is a clustered table created from `externalttitlebasics` and clustered by `tconst`,`titletype`
     - titleepisode - This is a clustered table created from `externalttitleepisode` and clustered by `tconst`,`parentTconst`
     - titleratings - This is a clustered table created from `externalttitleratings` and clustered by `tconst`
 
 **_Congratulations, Now we have built a successful data pipeline for downloading and ingesting the raw dataset to GCS. Also, to create an external and partitioned/Clustered tables in BigQuery!!_**
