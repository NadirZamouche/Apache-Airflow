from airflow.sdk import dag, task
from datetime import timedelta
import pendulum
from airflow.providers.postgres.hooks.postgres import PostgresHook
import csv
import logging
import os


default_args = {
    "owner": "airflow",
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}


@dag(
    dag_id="Postgres_Hook_DAG",
    default_args=default_args,
    start_date=pendulum.datetime(2026, 2, 12, 1, 45, tz="Africa/Algiers"),
    schedule="0 0 * * *",
    catchup=False,  # beginner friendly
)
def read__data_from_postgres_taskflow():
    @task()
    def get_data():
        today = pendulum.today().date()

        hook = PostgresHook(postgres_conn_id="postgres_localhost")
        conn = hook.get_conn()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM orders WHERE date = %s",
            (today,),
        )

        base_path = "/opt/airflow/data"
        os.makedirs(base_path, exist_ok=True)
        file_path = f"{base_path}/Orders_{today}.txt"

        with open(file_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([i[0] for i in cursor.description])
            writer.writerows(cursor.fetchall())

        cursor.close()
        conn.close()

        logging.info("Saved orders data in text file: %s", file_path)

    get_data()


# instantiate the DAG
dag = read__data_from_postgres_taskflow()
