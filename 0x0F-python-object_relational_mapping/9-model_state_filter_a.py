#!/usr/bin/python3
"""
script that lists all State objects that contain the letter a from
the database hbtn_0e_6_usa
    - script takes 3 arguments: mysql username, mysql password and databasename
    - uses the module SQLAlchemy
    - import State and Base from model_state
    - script connects to a MySQL server running on localhost at port 3306
    - Results sorted in ascending order by states.id
"""

if __name__ == '__main__':
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    s = Session()

    result = s.query(State).filter(State.name.like('%a%')).order_by(State.id)
    for a in result:
        print("{}: {}".format(a.id, a.name))
