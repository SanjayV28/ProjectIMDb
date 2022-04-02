# Data Pipeline Orchestration

There are plenty of workflow orchestration tools (like Airflow, Prefect, Luigi) available to setup our data pipelines. I have used Apache Airflow to setup the data pipelines for this project. In Airflow, we can define DAGs in python to setup our data pipelines. 

## Installation
Installing Airflow is quite challenging, the best practice is to install it with Docker. Please make sure that you have installed Docker and Docker Compose (Refer project prerequisites) and follow the instructions mentioned [here](https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html) for installing airflow.

## Running Airflow with Docker
Now we have successfully completed the Docker setup. We can start our data pipelines by following the below steps.

- In the cloned repository, Navigate to the airflow directory.
  ```
  cd airflow
  ```
- Setting up the user ID and neccessary folders for airflow.
  > **Note:** Make sure you are running the below commands in your IDE terminal
  ```
  mkdir -p ./dags ./logs ./plugins
  echo -e "AIRFLOW_UID=$(id -u)" > .env
  ```
- To Standarise the credentials, rename the service account json file as `google_credentials.json` and move it to `~/.google/credentials/` in your home directory.
- Set the environment variables for the below GCP resoucers in your Docker file.
  - GCP Project ID = **Project-ID**
  - Google Cloud Storage Bucket Name = **Bucket-Name**
  - GCP BigQuery Dataset Name = **Dataset-Name**
- Start the airflow by building the image (only first-time, or when there's any change in the Dockerfile, takes ~15 mins for the first-time)
  ```
  docker-compose build
  ```
- When you have successfully built the image, kick start all the related services from the container
  ```
  docker-compose up
  ```
- In another terminal, run `docker-compose ps` to see which containers are up & running healthy.
- Now we have successfully completed the Airflow setup. Login to Airflow web UI on `localhost:8080` with the default credentials.
  - User Name: **airflow**
  - Password: **airflow**
  
 - Trigger/Run your DAGs on the Web Console.
 - Once your pipelines are completed successfully, shut down the containers.
    ```
    docker-compose down
    ```
 ## DAGs
 
 For this project, We will setup the below four DAGs. 
 - `titleakas_dag.py`, `titlebasics_dag.py`, `titleepisode_dag.py` and `titleratings_dag.py`
   - These DAGs will download the raw datasets from the IMDb Wbsite and uncompress it. 
   - Convert the uncompressed datasets to parquet format.
   - Upload the converted parquet file into Google Cloud Storage Bucket. 
   - Create an external tables from the parquet files.
   - Create a partioned/clustered tables from the external tables by partioning/clustering the columns.
 
 - DAGs Flow:
   >**Note: These DAGs are scheduled to run on a daily basis because the IMDb source data is refreshed daily**.
   
   Pending
   
