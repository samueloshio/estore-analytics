from airflow.decorators import dag, task
from datetime import datetime

from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateEmptyDatasetOperator
@dag(
    start_date=datetime(2024,4,1),
    schedule=None,
    catchup=False,
    tags=['estore'],
)
def estore():
    upload_csv_to_gcs = LocalFilesystemToGCSOperator(
        task_id='upload_csv_to_gcs',
        src='/usr/local/airflow/include/database/estore.csv',
        dst='raw_data/estore.csv',
        bucket='estore-data_dtc-de-414207',
        gcp_conn_id='gcp',
        mime_type='text/csv'
    )

    create_retail_dataset = BigQueryCreateEmptyDatasetOperator(
        task_id="create_retail_dataset",
        dataset_id="estore_schema",
        gcp_conn_id="gcp",
        if_exists="ignore",
    )

estore()
