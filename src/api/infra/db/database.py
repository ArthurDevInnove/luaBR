from sqlalchemy import create_engine
from dotenv import load_dotenv
from os import getenv

load_dotenv()
DATABASE_USERNAME = getenv("DATABASE_USERNAME")
DATABASE_PASSWORD = getenv("DATABASE_PASSWORD")
DATABASE_PORT = getenv("PORT")

SQLALCHEMY_DATABASE_URL = f'mysql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@localhost:{DATABASE_PORT}/luabr'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True
)