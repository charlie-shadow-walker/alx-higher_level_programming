#!/usr/bin/python3


"""model - creating the model states"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

""" class state that inherits from the base class"""


class State(Base):

    """ initializing the table and its columns"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
