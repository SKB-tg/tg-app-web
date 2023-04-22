import logging

import sqlalchemy
from databases import Database
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database


from .settings import settings


#db = Database(settings.DB_URL)
engine = sqlalchemy.create_engine(settings.DB_URL, connect_args={"check_same_thread": False})# pool_size=3, max_overflow=0)
if not database_exists(engine.url):
    create_database(engine.url)
metadata = sqlalchemy.MetaData()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#metadata.create_all(engine)


def get_db():
    """
    A dependency for working with PostgreSQL
    """
    try:
        db = SessionLocal()
        yield db
    except Exception as e:
        logging.error(e)
    finally:
        db.close()