#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
"""
import sys
import MySQLdb

def list_states(username, password, database):
    """
    Function to list all states from the database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): MySQL database name.

    Returns:
        list: A list of tuples containing state information.
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

    # Execute the query
    cursor.execute("SELECT * FROM states ORDER BY id")

    # Fetch all the rows
    states = cursor.fetchall()

    # Display results
    for state in states:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1:]

    list_states(username, password, database)
