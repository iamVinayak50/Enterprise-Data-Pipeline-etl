from airflow import DAG
from airflow.providers.google.cloud.operators.dataproc import (
    DataprocCreateClusterOperator,
    DataprocSubmitJobOperator,
    DataprocDeleteClusterOperator
)
from airflow.operators.email_operator import EmailOperator
from airflow.utils.trigger_rule import TriggerRule
from datetime import datetime, timedelta


PROJECT_ID = "boxwood-axon-470816-b1"
REGION = "us-central1"
CLUSTER_NAME = "bq-mysql-cluster"
PYSPARK_URI = "gs://cars-demo-temp/pyspark/bq_to_mysql.py"  


default_args = {
    "owner": "vinayak",
    "depends_on_past": False,
    "email": ["vinayakshegar50@gmail.com"],
    "email_on_failure": False,  # we handle failure manually
    "email_on_retry": False,
    "retries": 0,
    "retry_delay": timedelta(minutes=2),
}

with DAG(
    "bq_to_mysql_jdbc_dataproc",
    default_args=default_args,
    start_date=datetime(2024, 11, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    # ------------------------------------------
    # 1. CREATE DATAPROC CLUSTER
    # ------------------------------------------
    create_cluster = DataprocCreateClusterOperator(
        task_id="create_cluster",
        project_id=PROJECT_ID,
        region=REGION,
        cluster_name=CLUSTER_NAME,
        cluster_config={
            "master_config": {
                "num_instances": 1,
                "machine_type_uri": "n1-standard-4"
            },
            "worker_config": {
                "num_instances": 2,
                "machine_type_uri": "n1-standard-4"
            }
        }
    )

    # ------------------------------------------
    # 2. SUBMIT PYSPARK JOB
    # ------------------------------------------
    submit_pyspark = DataprocSubmitJobOperator(
        task_id="submit_pyspark",
        project_id=PROJECT_ID,
        region=REGION,
        job={
            "reference": {"project_id": PROJECT_ID},
            "placement": {"cluster_name": CLUSTER_NAME},
            "pyspark_job": {
                "main_python_file_uri": PYSPARK_URI
            },
        }
    )

    # ------------------------------------------
    # 3. DELETE CLUSTER (ALWAYS RUN)
    # ------------------------------------------
    delete_cluster = DataprocDeleteClusterOperator(
        task_id="delete_cluster",
        project_id=PROJECT_ID,
        region=REGION,
        cluster_name=CLUSTER_NAME,
        trigger_rule=TriggerRule.ALL_DONE,  # Always delete cluster
    )

    

    # DAG FLOW
    create_cluster >> submit_pyspark >> delete_cluster 
