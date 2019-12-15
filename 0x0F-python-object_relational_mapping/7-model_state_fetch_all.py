#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    # Session.configure(bind=engine)
    session = Session()

    for row in session.query(State).order_by(State.id):
        print("{}: {}".format(row.id, row.name))
