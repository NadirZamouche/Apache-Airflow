from airflow import DAG
from datetime import timedelta
from airflow.operators.bash import BashOperator
import pendulum


default_args = {
    "owner": "airflow",
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

with DAG(
    dag_id="first_DAG",
    default_args=default_args,
    description="This is my first DAG",
    start_date=pendulum.datetime(2026, 2, 2, 17, 2, tz="Africa/Algiers"),
    schedule="*/2 * * * *",
    catchup=False,  # beginner friendly
) as dag:
    task1 = BashOperator(
        task_id="first_task", bash_command="echo hello world, this is my first task"
    )

    task1
