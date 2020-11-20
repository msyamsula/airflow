from sqlalchemy import create_engine, MetaData, Table

uri = "mysql://airflow:airflow@localhost:3306/source_db"
engine = create_engine(uri)
metadata = MetaData(engine)
conn = engine.connect()

Users = Table("users", metadata, autoload=True)
Accounts = Table("accounts", metadata, autoload=True)
FullService = Table("full_service", metadata, autoload=True)
