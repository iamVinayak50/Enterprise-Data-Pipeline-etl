from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from plugins.operators.api_operator import fetch_api_data
from plugins.operators.bq_operator import load_to_bq
from plugins.helpers.transform import transform_api_data

def etl_api_to_bq():
    data = fetch_api_data("https://api.publicapis.org/entries")
    df = transform_api_data(data)
    load_to_bq(df, "your_project.your_dataset.api_table")

with DAG("extract_api_to_bq", start_date=datetime(2025,10,13), schedule_interval="@daily", catchup=False) as dag:
    task = PythonOperator(task_id="etl_api", python_callable=etl_api_to_bq)
