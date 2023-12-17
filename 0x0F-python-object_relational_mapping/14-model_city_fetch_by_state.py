#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    # cities = session.query(City).join(State).order_by(City.id).all()
    cities = session.query(City, State).\
        join(State, State.id == City.state_id).all()
    if cities:
        for city, state in cities:
            print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
