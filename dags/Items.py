from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
from tasks import extractItemFromPrize, loadTableItems

# start_date = datetime.now() - timedelta(days=1, seconds=5)
start_date = datetime(2020,11,15,0)

default_args = {
    "start_date": start_date,
    "owner": "airflow"
}

with DAG(dag_id="linkajaItems_dag", schedule_interval="*/3 * * * *", default_args=default_args, catchup=False) as dag:

    # extraction
    extract = PythonOperator(task_id="extractItems", python_callable=extractItemFromPrize.main)

    # loading
    load = PythonOperator(task_id="loadItems", python_callable=loadTableItems.main)

    # dag
    extract >> load