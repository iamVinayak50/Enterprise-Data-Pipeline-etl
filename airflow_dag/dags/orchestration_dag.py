from airflow import DAG
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from airflow.utils.dates import days_ago

with DAG(
    "orchestration_dag",
    schedule_interval="0 12 * * *",
    start_date=days_ago(1),
    catchup=False
) as dag:

    trigger_dataform = TriggerDagRunOperator(
        task_id="trigger_dataform_dag",
        trigger_dag_id="dataform_dag",
        wait_for_completion=True
    )

    trigger_dataproc = TriggerDagRunOperator(
        task_id="trigger_dataproc_dag",
        trigger_dag_id="dataproc_dag",
        wait_for_completion=True
    )

    trigger_dataform >> trigger_dataproc
