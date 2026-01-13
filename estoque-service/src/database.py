import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

load_dotenv()
database_url = os.getenv('DATABASE_URL')


#url para testes
#database_url = "postgresql+psycopg2://postgres:1234@localhost:5432/MS-Estoque"

engine = create_engine(database_url)

Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def get_session():
    return Session()

