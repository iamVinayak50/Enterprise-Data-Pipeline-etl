from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from plugins.operators.bq_operator import query_bq_to_df, load_to_bq

def etl_bq_other_to_bq():
    df = query_bq_to_df("SELECT * FROM `other_project.dataset.table`")
    load_to_bq(df, "your_project.your_dataset.other_table")

with DAG("extract_bq_other_to_bq", start_date=datetime(2025,10,13), schedule_interval="@daily", catchup=False) as dag:
    task = PythonOperator(task_id="etl_bq_other", python_callable=etl_bq_other_to_bq)
