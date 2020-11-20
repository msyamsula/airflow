import pandas as pd

def add(row):
    return row['balance']+row['point']*10

def string_to_bool(row):
    if row['is_active']=="yes":
        return 1
    
    return 0

def main():
    # start pandas df, by reading from buffer csv
    buffer_dir = "/Users/muhammadsyamsularifin/airflow/buffer_data/users.csv"
    df = pd.read_csv(buffer_dir)

    # change username into user
    column_transformation = {
        "username": "user"
    }
    df = df.rename(columns=column_transformation)

    # drop domicile
    df = df.drop(columns=["domicile"])

    # create new column "net_worth"
    net_worth = df.apply(lambda row : add(row), axis=1)
    df["net_worth"] = net_worth

    # change is_active into bool
    is_active = df.apply(lambda row : string_to_bool(row), axis=1)
    df["is_active"] = is_active

    # save to buffer
    buffer_dir = "/Users/muhammadsyamsularifin/airflow/buffer_data/users_transformed.csv"
    df.to_csv(buffer_dir, index=False)

if __name__ == "__main__":
    main()