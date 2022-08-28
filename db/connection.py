import os
from dotenv import load_dotenv, find_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv(find_dotenv())

connection_string = (
    f'DRIVER={os.getenv("DATABASE_DRIVER")};'
    f'SERVER={os.getenv("DATABASE_SERVER")};'
    f'PORT={os.getenv("DATABASE_PORT")};'
    f'DATABASE={os.getenv("DATABASE_NAME")};'
    f'UID={os.getenv("DATABASE_USER")};'
    f'PWD={os.getenv("DATABASE_PASS")}'
)

connection_url = URL('mssql+pyodbc', query={'odbc_connect': connection_string})

engine = create_engine(connection_url, echo=False)

base = declarative_base()

session = sessionmaker(bind=engine)()
