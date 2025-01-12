import psycopg
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine
from config import settings


engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True, # all SQL-queries will be logged in console
    # pool_size=5, # maximum number of connections in connection pool
    # max_overflow=10 # additional connections
)

session_factory = sessionmaker(bind=engine)
