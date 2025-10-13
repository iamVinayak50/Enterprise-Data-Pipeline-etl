from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from plugins.operators.gcs_operator import read_gcs_json
from plugins.operators.bq_operator import load_to_bq

def etl_gcs_to_bq():
    df = read_gcs_json("your_bucket", "file.json")
    load_to_bq(df, "your_project.your_dataset.gcs_table")

with DAG("extract_gcs_to_bq", start_date=datetime(2025,10,13), schedule_interval="@daily", catchup=False) as dag:
    task = PythonOperator(task_id="etl_gcs", python_callable=etl_gcs_to_bq)
