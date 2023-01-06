from database import Base, session
from sqlalchemy import Column, Integer, String


class User(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(length=125), required=True)
