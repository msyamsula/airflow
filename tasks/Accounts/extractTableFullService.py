import pandas as pd
from connection.source import conn, FullService
from sqlalchemy.sql import select

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