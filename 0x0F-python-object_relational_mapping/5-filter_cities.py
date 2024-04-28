#!/usr/bin/python3
"""
This script lists all cities of a given state from the database hbtn_0e_4_usa.
"""
import sys
import MySQLdb

def list_cities_by_state(username, password, database, state_name):
    """
    Function to list all cities of a given state from the database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): MySQL database name.
        state_name (str): Name of the state to search for.
    """
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object
    cursor = db.cursor()

    # Prepare the query with a placeholder for the state name
    query = "SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id"

    # Execute the query with the state name as a parameter
    cursor.execute(query, (state_name,))

    # Fetch all the rows
    cities = cursor.fetchall()

    # Extract city names from the result
    city_names = [city[0] for city in cities]

    # Display results
    print(', '.join(city_names))

    # Close the cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:]

    list_cities_by_state(username, password, database, state_name)
