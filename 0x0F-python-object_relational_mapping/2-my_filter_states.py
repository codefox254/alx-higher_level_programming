#!/usr/bin/python3
"""
This script displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
"""
import sys
import MySQLdb # type: ignore

def search_states_by_name(username, password, database, state_name):
    """
    Function to search for states by name in the database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): MySQL database name.
        state_name (str): State name to search for.
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

    # Format the SQL query with user input
    query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id"
    cursor.execute(query, (state_name,))

    # Fetch all the rows
    states = cursor.fetchall()

    # Display results
    for state in states:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:]

    search_states_by_name(username, password, database, state_name)
