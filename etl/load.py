import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

def get_engine():
    url = os.getenv("TARGET_DB_URL")
    if not url:
        raise RuntimeError("TARGET_DB_URL is not configured in .env")
    return create_engine(url, pool_pre_ping=True)

def load_to_mysql(df, table_name="customers"):
    engine = get_engine()
    df.to_sql(table_name, engine, if_exists="append", index=False, method="multi")
