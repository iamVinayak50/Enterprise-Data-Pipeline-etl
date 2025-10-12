from airflow import DAG
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2025, 10, 13),
    'retries': 1,
}

with DAG(
    dag_id='daily_bq_transfer_data_cross_project',
    schedule_interval='@daily',
    default_args=default_args,
    catchup=False,
    tags=['bigquery', 'cross_project'],
) as dag:

    transfer_raw_car_specs = BigQueryInsertJobOperator(
        task_id='transfer_data_cross_project',
        configuration={
            "query": {
                "query": """
                    CREATE OR REPLACE TABLE `boxwood-axon-470816-b1.bronze_dataset.raw_car_specs`
                    AS
                    SELECT * FROM `helical-gist-445906-k3.bronze_dataset.raw_car_specs`
                    
                    CREATE OR REPLACE TABLE `boxwood-axon-470816-b1.bronze_dataset.raw_dealer_info`
                    AS
                    SELECT * FROM `helical-gist-445906-k3.bronze_dataset.raw_dealer_info`
                    
                    CREATE OR REPLACE TABLE `boxwood-axon-470816-b1.bronze_dataset.raw_sales_data`
                    AS
                    SELECT * FROM `helical-gist-445906-k3.bronze_dataset.raw_sales_data`
                """,
                "useLegacySql": False,
            }
        },
        location='US'
    )