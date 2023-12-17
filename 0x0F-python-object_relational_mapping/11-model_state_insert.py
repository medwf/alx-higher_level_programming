#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session = Session(engine)
    StateName = "Louisiana"
    session.add(State(name=StateName))
    session.commit()
    state = session.query(State).filter(State.name == StateName).first()
    print("{}".format(state.id))
    session.close()
