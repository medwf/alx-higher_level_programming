#!/usr/bin/python3
""" import file """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
""" DOC """

Base = declarative_base()


class State(Base):
    """ class State """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
