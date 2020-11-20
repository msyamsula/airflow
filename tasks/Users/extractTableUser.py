import pandas as pd
from sqlalchemy.sql import Select
from connection.source import conn, Users

def main(**kwargs):
    # use ti for xcom push and pull
    ti = kwargs["ti"]
    # try to read user buffer csv
    # if not found set param_id = 0
    user_id = 0
    buffer_dir = "/Users/muhammadsyamsularifin/airflow/buffer_data/users.csv"
    try:
        df = pd.read_csv(buffer_dir)
        user_id = int(df.tail(1)["id"])
    except FileNotFoundError:
        pass
    
    # select data from db, with id greater than variable "user_id"
    query = Select([Users]).where(Users.c.id>user_id).limit(3)
    result = conn.execute(query)

    # prepare pandas dataframe, new and empty
    column = [
        "id",
        "username",
        "address",
        "is_active",
        "domicile",
        "balance",
        "point"
    ]
    df = pd.DataFrame(columns=column)

    # insert it into pandas
    for id, username, address, is_active, domicile, balance, point in result:
        new_row = {
            "id": id,
            "username": username,
            "address": address,
            "is_active": is_active,
            "domicile": domicile,
            "balance": float(balance),
            "point": float(point)
        }
        df = df.append(new_row, ignore_index=True)

    # if no data extracted, tell xcom that it is done
    if (len(df["id"]) == 0):
        ti.xcom_push(key="extract_user_done", value=1)
        return None

    # save to csv file
    buffer_dir = "/Users/muhammadsyamsularifin/airflow/buffer_data/users.csv"
    df.to_csv(buffer_dir, index=False)