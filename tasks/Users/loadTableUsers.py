import pandas as pd
from connection.sink import conn

def main():
    # load pandas dataframe
    buffer_dir = "/Users/muhammadsyamsularifin/airflow/buffer_data/users_transformed.csv"
    df = pd.read_csv(buffer_dir)
    df = df.set_index('id')

    print(df)

    # load to database
    df.to_sql(con=conn, name="users", if_exists="append")

if __name__ == "__main__":
    main()