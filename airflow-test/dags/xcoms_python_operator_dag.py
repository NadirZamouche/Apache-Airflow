from airflow import DAG
from datetime import timedelta
from airflow.operators.python import PythonOperator
import pendulum


default_args = {
    "owner": "airflow",
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}


def get_name():
    return "Wagner"


def begrüßung(ti):
    name = ti.xcom_pull(task_ids="get_name")
    print(f"Herr {name} Herzlich Willkommen!")


with DAG(
    dag_id="XComs_python_operator_DAG",
    default_args=default_args,
    start_date=pendulum.datetime(2026, 2, 4, 15, 28, tz="Africa/Algiers"),
    schedule="*/2 * * * *",
    catchup=False,  # beginner friendly
) as dag:
    task1 = PythonOperator(task_id="get_name", python_callable=get_name)
    task2 = PythonOperator(task_id="Begrüßung", python_callable=begrüßung)

    task1 >> task2
