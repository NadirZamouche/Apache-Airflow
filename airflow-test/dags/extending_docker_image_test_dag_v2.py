from airflow.decorators import dag, task
from datetime import timedelta
import pendulum

default_args = {
    "owner": "airflow",
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}


@dag(
    dag_id="Extending_Docker_Image_Test_DAG_v2",
    default_args=default_args,
    start_date=pendulum.datetime(2026, 2, 10, 3, 50, tz="Africa/Algiers"),
    schedule="*/5 * * * *",
    catchup=False,  # beginner friendly
)
def hello_world_etl():
    @task()
    def get_sklearn():
        import sklearn

        print(f"Sklearn version: {sklearn.__version__}")

    @task()
    def get_pandas():
        import pandas

        print(f"Pandas version: {pandas.__version__}")

    get_sklearn()
    get_pandas()


dag = hello_world_etl()
