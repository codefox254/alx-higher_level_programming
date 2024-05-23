#!/usr/bin/python3
"""Script to create the State "California" with the City "San Francisco"
in the database hbtn_0e_100_usa."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


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

    # Create State "California" and City "San Francisco"
    california = State(name="California", cities=[City(name="San Francisco")])

    # Add State and City to session and commit changes
    session.add(california)
    session.commit()

    # Close session
    session.close()
