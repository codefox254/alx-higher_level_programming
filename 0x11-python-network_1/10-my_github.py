#!/usr/bin/python3
"""
This script takes GitHub username and password (personal access token) as input and uses Basic Authentication with a personal access token to access the GitHub API and display the user's ID.
"""

if __name__ == '__main__':
    from requests import get
    from sys import argv

    username = argv[1]
    password = argv[2]

    URL = "https://api.github.com/user"
    response = get(URL, auth=(username, password))
    json = response.json()

    print(json.get('id'))