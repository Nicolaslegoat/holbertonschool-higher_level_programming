#!/usr/bin/python3
"""
class definition of a CIty and an instance Base = declarative_base()
"""

from model_state import Base
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """ """
    __tablename__ = "cities"
    id = Column(Integer, primarykey=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
