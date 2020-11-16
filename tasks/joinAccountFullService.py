import pandas as pd

def add(row):
    return row['balance']+row['point']*10

def string_to_bool(row):
    # print(row["is_active"]=="yes", row["is_active"], "yes")
    if row['is_active']=="yes":
        return 1
    
    return 0

def main():
    # start pandas df, by reading from buffer csv
    buffer_dir = "/Users/muhammadsyamsularifin/airflow/buffer_data/accounts.csv"
    df_account = pd.read_csv(buffer_dir)
    buffer_dir = "/Users/muhammadsyamsularifin/airflow/buffer_data/full_service.csv"
    df_full_service = pd.read_csv(buffer_dir)

    # join two df
    df_join = df_account.set_index("id").join(df_full_service.set_index("account_id"))

    # rename to appropriate column name
    df_join["full_service"] = df_join["is_full"]
    df_join = df_join.drop(columns=["is_full"])

    # save to buffer_data
    buffer_dir = "/Users/muhammadsyamsularifin/airflow/buffer_data/joinAccountFullService.csv"
    df_join.to_csv(buffer_dir)

if __name__ == "__main__":
    main()