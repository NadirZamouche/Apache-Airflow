from airflow.decorators import dag, task
from datetime import timedelta
import pendulum


default_args = {
    "owner": "airflow",
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}


@dag(
    dag_id="TaskFlow_API_Multi_Param_DAG_v2",
    default_args=default_args,
    start_date=pendulum.datetime(2026, 2, 4, 17, 54, tz="Africa/Algiers"),
    schedule="*/2 * * * *",
    catchup=False,  # beginner friendly
)
def hello_world_etl():
    @task(multiple_outputs=True)
    def get_name():
        return {"first_name": "Nad", "last_name": "Zam"}

    @task()
    def get_age():
        return 23

    @task()
    def greet(first_name, last_name, age):
        print(
            f"Herzlich Willkommen! Herr {first_name} {last_name}, Sie sind ja {age} Jahre alt?"
        )

    name_dict = get_name()
    age = get_age()
    greet(first_name=name_dict["first_name"], last_name=name_dict["last_name"], age=age)


greet_dag = hello_world_etl()
