from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from plugins.operators.bq_operator import query_bq_to_df
from plugins.operators.mysql_operator import load_mysql_table

def load_bq_to_mysql():
    df = query_bq_to_df("SELECT * FROM `your_project.your_dataset.api_table`")
    engine_url = "mysql+pymysql://user:pass@host:3306/db"
    load_mysql_table(df, "mysql_table", mode="truncate", engine_url=engine_url)

with DAG("bq_to_mysql", start_date=datetime(2025,10,13), schedule_interval="@daily", catchup=False) as dag:
    task = PythonOperator(task_id="bq_to_mysql_task", python_callable=load_bq_to_mysql)
