from airflow import DAG
from datetime import timedelta
from airflow.operators.python import PythonOperator
import pendulum


default_args = {
    "owner": "airflow",
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}


def begrüßung():
    print("Herzlich Willkommen!")


with DAG(
    dag_id="python_operator_DAG_v1",
    default_args=default_args,
    description="This is my first DAG using python operator",
    start_date=pendulum.datetime(2026, 2, 2, 17, 42, tz="Africa/Algiers"),
    schedule="*/2 * * * *",
    catchup=False,  # beginner friendly
) as dag:
    task = PythonOperator(task_id="Begrüßung", python_callable=begrüßung)

    task
