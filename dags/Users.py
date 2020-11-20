from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator, BranchPythonOperator
from airflow.operators.dummy_operator import DummyOperator
from tasks.Users import extractTableUser, branching, loadTableUsers, tranformTableUser

start_date = datetime(2020,11,15,0)

default_args = {
    "start_date": start_date,
    "owner": "airflow"
}

with DAG(dag_id="linkajaUser_dag", schedule_interval="*/3 * * * *", default_args=default_args, catchup=False) as dag:

    # extraction
    extractUser = PythonOperator(task_id="extractUser", python_callable=extractTableUser.main, provide_context=True)

    # branching after extraction
    branching = BranchPythonOperator(task_id="branching", python_callable=branching.main, provide_context=True)

    # done
    done = DummyOperator(task_id="done")

    # transformation
    transformUser = PythonOperator(task_id="transformUser", python_callable=tranformTableUser.main)

    # loading
    loadUser = PythonOperator(task_id="loadUser", python_callable=loadTableUsers.main)

    # dag
    extractUser >> branching
    branching >> transformUser
    branching >> done
    transformUser >> loadUser