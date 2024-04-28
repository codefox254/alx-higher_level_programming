#!/usr/bin/python3
"""Script to add the State object "Louisiana" to the database hbtn_0e_6_usa."""
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

    # Create State object for Louisiana
    louisiana = State(name="Louisiana")

    # Add State object to session and commit changes to database
    session.add(louisiana)
    session.commit()

    # Print the new state's id
    print(louisiana.id)

    # Close session
    session.close()
