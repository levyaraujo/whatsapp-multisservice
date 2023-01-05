from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.config import settings

engine = create_engine(settings.URL, echo=True, future=True)
Session = sessionmaker(engine)
session = Session()
Base = declarative_base()


def init():
    Base.metadata.create_all(engine)
