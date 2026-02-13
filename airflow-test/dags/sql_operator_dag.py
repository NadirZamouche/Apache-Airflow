from airflow.decorators import dag
from datetime import timedelta
import pendulum
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator


default_args = {
    "owner": "airflow",
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}


@dag(
    dag_id="SQL_Operator_DAG",
    default_args=default_args,
    start_date=pendulum.datetime(2026, 2, 9, 4, 36, tz="Africa/Algiers"),
    schedule="*/2 * * * *",
    catchup=False,  # beginner friendly
)
def hello_world_etl():
    task1 = SQLExecuteQueryOperator(
        task_id="create_table",
        conn_id="postgres_localhost",
        sql="""
            CREATE TABLE IF NOT EXISTS dag_runs (
                dt DATE,
                dag_id VARCHAR(255)
            );
        """,
    )
    task2 = SQLExecuteQueryOperator(
        task_id="insert_data",
        conn_id="postgres_localhost",
        sql="""
            insert into dag_runs (dt, dag_id)
            VALUES ('{{ ds }}', '{{ dag.dag_id }}');
        """,
    )
    task1 >> task2  # setting dependencies


# instantiate the DAG
dag = hello_world_etl()
