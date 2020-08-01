from sqlalchemy import Boolean, Column, Integer, String  # type: ignore

from .db import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    enabled = Column(Boolean, default=True)
