from airflow.operators import python_operator, PythonOperator
from airflow.models import DAG
from datetime import datetime, timedelta


# input to dag (workflow)
args = {
    'owner': 'syamsul',
    'start_date': datetime(2020,11,15),
    'retries': 2,
    'retry_dely': timedelta(minutes=1)
}

# dag (workflow) with name dags, and have parameter args
dags = DAG('test_dag', default_args=args)

# function that will be executed by dag (workflow)
def print_context(val):
    print(val)

def print_text():
    print("hello")

# python operator, call print_context with parameter=op_kwargs, id = multitask1
t1 = PythonOperator(task_id='multitask1', op_kwargs={'val': {'a':1,'b':2}}, python_callable=print_context, dag=dags)
# python operator, call print_text, without any parameter, id = multitast2
t2 = PythonOperator(task_id='multitask2', python_callable=print_text, dag=dags)
t2.set_upstream(t1)