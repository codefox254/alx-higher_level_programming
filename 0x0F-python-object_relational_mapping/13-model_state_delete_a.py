#!/usr/bin/python3
"""Script to delete all State objects with a name containing the letter "a"
   from the database hbtn_0e_6_usa."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Extract command-line arguments
    username, password, database = sys.argv[1:]

    # Create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and delete State objects with names containing letter "a"
    states_with_a = session.query(State).filter(State.name.like('%a%')).all()
    if states_with_a:
        for state in states_with_a:
            session.delete(state)
        session.commit()
        print("State objects with names containing 'a' deleted successfully")
    else:
        print("No State objects with names containing 'a' found")

    # Close session
    session.close()
