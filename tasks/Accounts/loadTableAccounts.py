import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, select
from sqlalchemy.sql import select
from connection.sink import conn

def main():
    # load pandas dataframe
    buffer_dir = "/Users/muhammadsyamsularifin/airflow/buffer_data/joinAccountFullService.csv"
    df = pd.read_csv(buffer_dir)
    df = df.set_index("id")
    
    # load to database
    df.to_sql(con=conn, name="accounts", if_exists="append")