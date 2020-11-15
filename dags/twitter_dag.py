# from airflow import DAG
# from airflow.contrib.sensors.file_sensor import FileSensor
# from datetime import datetime, timedelta
# from airflow.operators.python_operator import PythonOperator
# import fetching, cleaning, storing

# start_date = datetime.now() - timedelta(days=1, seconds=5)

# default_args = {
#     "start_date": start_date,
#     "owner": "airflow"
# }

# with DAG(dag_id="twitter_dag", schedule_interval="@daily", default_args=default_args, catchup=False) as dag:
#     # file sensor, to monitor file input.csv
#     # you need to configure connection with id fs_tweet in airflow webserver and specify the location fo filepath
#     watiting_for_tweets = FileSensor(task_id="waiting_for_tweet",fs_conn_id="fs_tweet", filepath="input.csv", poke_interval=5)

#     # fetching from input.csv and transfrom the data, load it into output.csv, using python code
#     fetching = PythonOperator(task_id="fetching", python_callable=fetching.main)

#     # cleaning data using python code
#     cleaning = PythonOperator(task_id="cleaning", python_callable=cleaning.main)

#     # storing data using python code
#     storing = PythonOperator(task_id="storing", python_callable=storing.main)

#     # dag
#     watiting_for_tweets >> fetching >> cleaning >> storing