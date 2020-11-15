import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, select
from sqlalchemy.sql import select

# set up db connection
uri = "mysql://airflow:airflow@localhost:3306/source_db"
engine = create_engine(uri)
metadata = MetaData(engine)
conn = engine.connect()

Users = Table("users", metadata, autoload=True)


def main():
    # select data from db,
    query = select([Users])
    result = conn.execute(query)

    # prepare pandas dataframe
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
        # print(df)
        df = df.append(new_row, ignore_index=True)

    # save to csv file
    buffer_dir = "/Users/muhammadsyamsularifin/airflow/buffer_data/users.csv"
    df.to_csv(buffer_dir, index=False)

if __name__ == "__main__":
    main()