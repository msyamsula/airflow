import pandas as pd
from datetime import datetime as dt

def main():
    tweets = pd.read_csv("~/airflow/data/input.csv", encoding="latin1")
    tweets = tweets.drop('rowid', axis=1)
    tweets.to_csv("~/airflow/data/output.csv", index=False)

if __name__ == "__main__":
    main()