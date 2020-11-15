import pandas as pd
from datetime import datetime as dt

def main():
    tweets = pd.read_csv("~/airflow/data/output.csv", encoding="latin1")
    tweets = tweets.drop('other', axis=1)
    tweets.to_csv("~/airflow/data/cleaned.csv", index=False)

if __name__ == "__main__":
    main()