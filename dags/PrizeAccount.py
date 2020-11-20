from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
from tasks.PrizeAccount import extractPrizeAccount, loadTablePrizeAccount

# start date
start_date = datetime(2020,11,15,0)

default_args = {
    "start_date": start_date,
    "owner": "airflow"
}

with DAG(dag_id="linkajaPrizeAccount_dag", schedule_interval="*/3 * * * *", default_args=default_args, catchup=False) as dag:

    # extraction
    extract = PythonOperator(task_id="extractUser", python_callable=extractPrizeAccount.main)

    # loading
    load = PythonOperator(task_id="loadUser", python_callable=loadTablePrizeAccount.main)

    # dag
    extract >> load