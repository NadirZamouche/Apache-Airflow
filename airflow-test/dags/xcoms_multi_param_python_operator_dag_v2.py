from airflow import DAG
from datetime import timedelta
from airflow.operators.python import PythonOperator
import pendulum


default_args = {
    "owner": "airflow",
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}


def get_name(ti):
    ti.xcom_push(key="first_name", value="Tino")
    ti.xcom_push(key="last_name", value="Chrupalla")


def begrüßung(ti):
    first_name = ti.xcom_pull(task_ids="get_name", key="first_name")
    last_name = ti.xcom_pull(task_ids="get_name", key="last_name")
    print(f"Herr {first_name} {last_name} Herzlich Willkommen!")


with DAG(
    dag_id="XComs_multi_param_python_operator_DAG_v2",
    default_args=default_args,
    start_date=pendulum.datetime(2026, 2, 4, 15, 42, tz="Africa/Algiers"),
    schedule="*/2 * * * *",
    catchup=False,  # beginner friendly
) as dag:
    task1 = PythonOperator(task_id="get_name", python_callable=get_name)
    task2 = PythonOperator(task_id="Begrüßung", python_callable=begrüßung)

    task1 >> task2
