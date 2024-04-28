#!/usr/bin/python3
"""Lists all City objects from the database hbtn_0e_101_usa."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City

def list_cities_states(username, password, database):
    """Lists all City objects with their corresponding State from the database."""
    # Create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all City objects with their corresponding State objects
    cities = session.query(City).order_by(City.id).all()

    # Print results
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    # Close session
    session.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)
    list_cities_states(sys.argv[1], sys.argv[2], sys.argv[3])
