import pandas as pd
from sqlalchemy import create_engine, MetaData, Table

# set up db connection
uri = "mysql://airflow:airflow@localhost:3306/test"
engine = create_engine(uri)
metadata = MetaData(engine)
conn = engine.connect()

tweets = Table("tweets", metadata, autoload=True)


def main():
    # get clean data
    data = pd.read_csv("~/airflow/data/cleaned.csv")
    name = data['name'].iloc[0]
    tweet = data['tweet'].iloc[0]

    # insert object
    ins = tweets.insert().values(name=name, tweet=tweet)

    # peek the sql syntax and params
    print(ins)
    print(ins.compile().params)

    # execute
    conn.execute(ins)


if __name__ == "__main__":
    main()