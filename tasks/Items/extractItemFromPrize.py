import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, select
from sqlalchemy.sql import select

# set up db connection
uri = "mysql://airflow:airflow@localhost:3306/source_db"
engine = create_engine(uri)
metadata = MetaData(engine)
conn = engine.connect()

Prize = Table("prize", metadata, autoload=True)


def main():
    # get data from buffer csv
    buffer_dir = "/Users/muhammadsyamsularifin/airflow/buffer_data/items.csv"

    # try to read user buffer csv
    # if not found set param_id = 0
    param_id = 0
    try:
        df = pd.read_csv(buffer_dir)
        param_id = int(df.tail(1)["item_id"])
    except FileNotFoundError:
        pass
    
    # select data from db, with id greater than variable "id"
    sql = f"SELECT DISTINCT item_id, item_name, value FROM prize WHERE item_id > {param_id} LIMIT 3"
    df = pd.read_sql(sql=sql, con=conn)

    # save to buffer
    buffer_dir = "/Users/muhammadsyamsularifin/airflow/buffer_data/items.csv"
    df.to_csv(buffer_dir, index=False)

if __name__ == "__main__":
    main()