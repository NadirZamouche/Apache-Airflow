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
    dag_id="first_DAG_v3",
    default_args=default_args,
    description="This is my first DAG",
    start_date=pendulum.datetime(2026, 2, 2, 17, 14, tz="Africa/Algiers"),
    schedule="*/2 * * * *",
    catchup=False,  # beginner friendly
) as dag:
    task1 = BashOperator(task_id="first_task", bash_command="echo Task Force 1")
    task2 = BashOperator(task_id="second_task", bash_command="echo Task Force 2")
    task3 = BashOperator(task_id="third_task", bash_command="echo Task Force 3")

    # Task dependency logic here is that task 3 is independent of task 2
    # Task dependency method 1
    # task1.set_downstream(task2)
    # task1.set_downstream(task3)

    # Task dependency method 2
    task1 >> task2
    task1 >> task3

    # Task dependency method 3
    # task1 >> [task2, task3]
