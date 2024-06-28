#!/usr/bin/python3
"""A python file that contains the class definition
of a State and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class State(Base):
    """A definition af a class state
    that inherits from Base
    """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
