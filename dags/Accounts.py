from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
from tasks.Accounts import extractTableAccount, extractTableFullService, transformAccountFullService, loadTableAccounts

# start_date = datetime.now() - timedelta(days=1, seconds=5)
start_date = datetime(2020,11,15,0)

default_args = {
    "start_date": start_date,
    "owner": "airflow"
}

with DAG(dag_id="linkajaAccount_dag", schedule_interval="*/3 * * * *", default_args=default_args, catchup=False) as dag:

    # extraction
    extractAccount = PythonOperator(task_id="extractAccount", python_callable=extractTableAccount.main)
    extractFullService = PythonOperator(task_id="extractFullService", python_callable=extractTableFullService.main)

    # transformation
    transformAccountFullService = PythonOperator(task_id="transformAccountFullService", python_callable=transformAccountFullService.main)

    # loading
    loadAccount = PythonOperator(task_id="loadAccount", python_callable=loadTableAccounts.main)

    # dag
    extractAccount >> transformAccountFullService >> loadAccount
    extractFullService >> transformAccountFullService >> loadAccount