import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, select
from sqlalchemy.sql import select

# set up db connection
uri = "mysql://airflow:airflow@localhost:3306/sink_db"
engine = create_engine(uri)
metadata = MetaData(engine)
conn = engine.connect()

# Users = Table("users", metadata, autoload=True)

def main():
    # load pandas dataframe
    buffer_dir = "/Users/muhammadsyamsularifin/airflow/buffer_data/joinAccountFullService.csv"
    df = pd.read_csv(buffer_dir)
    df = df.set_index("id")
    # load to database
    df.to_sql(con=conn, name="linkaja_account", if_exists="append")

if __name__ == "__main__":
    main()