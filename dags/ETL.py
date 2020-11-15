from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
from tasks import extractTableUser, loadTableUser, tranformTableUser

# start_date = datetime.now() - timedelta(days=1, seconds=5)
start_date = datetime(2020,11,15)

default_args = {
    "start_date": start_date,
    "owner": "airflow"
}

with DAG(dag_id="etl_dag", schedule_interval=None, default_args=default_args, catchup=False) as dag:

    # extraction
    extract = PythonOperator(task_id="extract", python_callable=extractTableUser.main)

    # transformation
    transform = PythonOperator(task_id="transform", python_callable=tranformTableUser.main)

    # loading
    load = PythonOperator(task_id="load", python_callable=loadTableUser.main)

    # dag
    extract >> transform >> load