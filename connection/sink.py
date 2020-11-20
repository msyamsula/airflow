from sqlalchemy import create_engine, MetaData, Table

# set up db connection
uri = "mysql://airflow:airflow@localhost:3306/sink_db"
engine = create_engine(uri)
metadata = MetaData(engine)
conn = engine.connect()