import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, select
from sqlalchemy.sql import select

# set up db connection
uri = "mysql://airflow:airflow@localhost:3306/source_db"
engine = create_engine(uri)
metadata = MetaData(engine)
conn = engine.connect()

FullService = Table("full_service", metadata, autoload=True)


def main():
    # get data from buffer csv
    buffer_dir = "/Users/muhammadsyamsularifin/airflow/buffer_data/full_service.csv"

    # try to read user buffer csv
    # if not found set param_id = 0
    param_id = 0
    try:
        df = pd.read_csv(buffer_dir)
        param_id = int(df.tail(1)["account_id"])
    except FileNotFoundError:
        pass
    
    # select data from db, with id greater than variable "id"
    query = select([FullService]).where(FullService.c.account_id>param_id).limit(4)
    result = conn.execute(query)

    # prepare pandas dataframe, new and empty
    column = [
        "account_id",
        "is_full"
    ]
    df = pd.DataFrame(columns=column)

    # insert it into pandas
    for account_id, is_full in result:
        new_row = {
            "account_id": account_id,
            "is_full": is_full
        }
        df = df.append(new_row, ignore_index=True)

    # save to csv file
    buffer_dir = "/Users/muhammadsyamsularifin/airflow/buffer_data/full_service.csv"
    df.to_csv(buffer_dir, index=False)

if __name__ == "__main__":
    main()