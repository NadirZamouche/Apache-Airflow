from airflow.decorators import dag, task
from datetime import timedelta
import pendulum


default_args = {
    "owner": "airflow",
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}


@dag(
    dag_id="TaskFlow_API_DAG_v1",
    default_args=default_args,
    start_date=pendulum.datetime(2026, 2, 4, 16, 11, tz="Africa/Algiers"),
    schedule="*/2 * * * *",
    catchup=False,  # beginner friendly
)
def hello_world_etl():
    @task()
    def get_name():
        return "Zam"

    @task()
    def get_age():
        return 23

    @task()
    def greet(name, age):
        print(f"Herzlich Willkommen! Herr {name}, Sie sind ja {age} Jahre alt?")

    name = get_name()
    age = get_age()
    greet(name=name, age=age)


greet_dag = hello_world_etl()
