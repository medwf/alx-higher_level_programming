#!/usr/bin/python3
""" import file """

from sqlalchemy import column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
""" DOC """

Base = declarative_base()


class State(Base):
    """ class State """
    __tablename__ = 'states'

    id = column(Integer, primary_key=True, nullable=False)
    name = column(String(128), nullable=False)
