#!/usr/bin/python3
"""
script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
    - script should take 4 arguments: mysql username, mysql password,
    database name and state name to search (SQL injection free)
    - uses the module SQLAlchemy
    - imports State and Base from model_state
    - script connects to a MySQL server running on localhost at port 3306
    - You can assume you have one record with the state name to search
    - Results must display the states.id
    - If no state has the name you searched for, display Not found
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                        argv[2], argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    state = session.query(State).filter_by(name=argv[4]).first()
    if state is not None:
        print(str(state.id))
    else:
        print("Not found")
