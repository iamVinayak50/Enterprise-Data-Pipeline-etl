from airflow import DAG
from airflow.providers.google.cloud.operators.dataproc import (
    DataprocCreateClusterOperator,
    DataprocSubmitJobOperator,
    DataprocDeleteClusterOperator,
)
from datetime import datetime

# -------------------------------
# DAG CONFIGURATION
# -------------------------------
PROJECT_ID = "boxwood-axon-470816-b1"
REGION = "us-central1"
CLUSTER_NAME = "jlr-temp-cluster"
PYSPARK_URI = "gs:// jlr_service_data/jlr-scripts/jlr_service_etl.py"

# -------------------------------
# DEFAULT ARGUMENTS
# -------------------------------
default_args = {
    "owner": "vinayak",
    "start_date": datetime(2025, 11, 10),
    "retries": 0,
}

# -------------------------------
# DEFINE DAG
# -------------------------------
with DAG(
    dag_id="jlr_dataproc_etl_dag",
    schedule_interval="@daily",
    default_args=default_args,
    catchup=False,
    tags=["dataproc", "jlr", "etl"],
) as dag:

    # 1️⃣ CREATE CLUSTER
    create_cluster = DataprocCreateClusterOperator(
        task_id="create_cluster",
        project_id=PROJECT_ID,
        region=REGION,
        cluster_name=CLUSTER_NAME,
        cluster_config={
            "master_config": {"num_instances": 1, "machine_type_uri": "n1-standard-2"},
            "worker_config": {"num_instances": 2, "machine_type_uri": "n1-standard-2"},
        },
    )

    # 2️⃣ SUBMIT PYSPARK JOB
    pyspark_job = {
        "reference": {"project_id": PROJECT_ID},
        "placement": {"cluster_name": CLUSTER_NAME},
        "pyspark_job": {"main_python_file_uri": PYSPARK_URI},
    }

    submit_job = DataprocSubmitJobOperator(
        task_id="submit_pyspark_job",
        project_id=PROJECT_ID,
        region=REGION,
        job=pyspark_job,
    )

    # 3️⃣ DELETE CLUSTER
    delete_cluster = DataprocDeleteClusterOperator(
        task_id="delete_cluster",
        project_id=PROJECT_ID,
        cluster_name=CLUSTER_NAME,
        region=REGION,
        trigger_rule="all_done",  # Delete even if job fails
    )

    # TASK ORDER
    create_cluster >> submit_job >> delete_cluster
