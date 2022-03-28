import os
import logging
import gzip
import shutil
from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

from google.cloud import storage
from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateExternalTableOperator, BigQueryInsertJobOperator
import pyarrow.csv as pv
import pyarrow.parquet as pq

PROJECT_ID = os.environ.get("GCP_PROJECT_ID")
BUCKET = os.environ.get("GCP_GCS_BUCKET")
BIGQUERY_DATASET = os.environ.get("GCP_DATASET")

dataset_file = "title.ratings.tsv"
dataset = "title.ratings.tsv.gz"
dataset_url = f"https://datasets.imdbws.com/{dataset}"
path_to_local_home = os.environ.get("AIRFLOW_HOME", "/opt/airflow/")
parquet_file = dataset_file.replace('.tsv', '.parquet')


def uncompress_dataset(src_file):
    with gzip.open(f'{src_file}', 'rb') as f_in:
        with open(f'{dataset_file}', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)


def format_to_parquet(src_file):
    if not src_file.endswith('.tsv'):
        logging.error("Can only accept source files in TSV format, for the moment")
        return
    table = pv.read_csv(src_file, parse_options=pv.ParseOptions(delimiter="\t"))
    pq.write_table(table, src_file.replace('.tsv', '.parquet'))


# NOTE: takes 20 minutes, at an upload speed of 800kbps. Faster if your internet has a better upload speed
def upload_to_gcs(bucket, object_name, local_file):
    """
    Ref: https://cloud.google.com/storage/docs/uploading-objects#storage-upload-object-python
    :param bucket: GCS bucket name
    :param object_name: target path & file-name
    :param local_file: source path & file-name
    :return:
    """
    # WORKAROUND to prevent timeout for files > 6 MB on 800 kbps upload speed.
    # (Ref: https://github.com/googleapis/python-storage/issues/74)
    storage.blob._MAX_MULTIPART_SIZE = 5 * 1024 * 1024  # 5 MB
    storage.blob._DEFAULT_CHUNKSIZE = 5 * 1024 * 1024  # 5 MB
    # End of Workaround

    client = storage.Client()
    bucket = client.bucket(bucket)

    blob = bucket.blob(object_name)
    blob.upload_from_filename(local_file)


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 1,
}

# NOTE: DAG declaration - using a Context Manager (an implicit way)
with DAG(
        dag_id="titleratings_dag",
        start_date=datetime(2022, 3, 23),
        schedule_interval="@once",
        default_args=default_args,
        catchup=False,
        max_active_runs=1,
        tags=['fp-de'],
) as dag:

    download_dataset_task = BashOperator(
        task_id="download_dataset_task",
        bash_command=f"curl -sS {dataset_url} > {path_to_local_home}/{dataset}"
    )

    uncompress_dataset_task = PythonOperator(
        task_id="uncompress_dataset_task",
        python_callable=uncompress_dataset,
        op_kwargs={
            "src_file": f"{path_to_local_home}/{dataset}",
        },
    )

    format_to_parquet_task = PythonOperator(
        task_id="format_to_parquet_task",
        python_callable=format_to_parquet,
        op_kwargs={
            "src_file": f"{path_to_local_home}/{dataset_file}",
        },
    )

    local_to_gcs_task = PythonOperator(
        task_id="local_to_gcs_task",
        python_callable=upload_to_gcs,
        op_kwargs={
            "bucket": BUCKET,
            "object_name": f"{parquet_file}",
            "local_file": f"{path_to_local_home}/{parquet_file}",
        },
    )

    bigquery_external_table_task = BigQueryCreateExternalTableOperator(
        task_id="bigquery_external_table_task",
        table_resource={
            "tableReference": {
                "projectId": PROJECT_ID,
                "datasetId": BIGQUERY_DATASET,
                "tableId": "externaltitleratings",
            },
            "externalDataConfiguration": {
                "sourceFormat": "PARQUET",
                "sourceUris": [f"gs://{BUCKET}/{parquet_file}"],
            },
        },
    )

    QUERY = f"""
    CREATE OR REPLACE TABLE sanjay-fp-de.raw.titleratings \
    CLUSTER BY tconst AS \
    SELECT * FROM `{PROJECT_ID}.{BIGQUERY_DATASET}.externaltitleratings`;
    """
    bigquery_PC_table_task = BigQueryInsertJobOperator(
        task_id="bigquery_PC_table_task",
        configuration={
            "query": {
                "query": QUERY,
                "useLegacySql": False,
            },
        },
    )

download_dataset_task >> uncompress_dataset_task >> format_to_parquet_task >> local_to_gcs_task >> bigquery_external_table_task >> bigquery_PC_table_task