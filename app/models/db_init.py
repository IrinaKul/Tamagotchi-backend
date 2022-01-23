from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

from app.config import Config

db = SQLAlchemy()


def get_engine_from_settings():
    url = Config.SQLALCHEMY_DATABASE_URI
    if not database_exists(url):
        create_database(url)
    engine = create_engine(url, pool_size=50, echo=False)
    return engine


def get_session():
    engine = get_engine_from_settings()
    session = sessionmaker(bind=engine)()
    return session
