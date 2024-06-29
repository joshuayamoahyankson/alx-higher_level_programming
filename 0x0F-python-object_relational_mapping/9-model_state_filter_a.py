#!/usr/bin/python3
"""A script that lists all State
objects from the database hbtn_0e_6_usa
"""

from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State

if __name__ == '__main__':
    """connects to the engine and retrieves needed information"""
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    db_connection = (
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            mysql_username, mysql_password, database_name
        )
    )
    engine = create_engine(db_connection, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = (
        session.query(State)
        .filter(State.name.ilike('%a%'))
        .order_by(State.id)
        .all()
    )
    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()
