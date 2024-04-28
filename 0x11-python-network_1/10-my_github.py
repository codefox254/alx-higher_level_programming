#!/usr/bin/python3
"""
This script takes GitHub username and password (personal access token) as input and uses Basic Authentication with a personal access token to access the GitHub API and display the user's ID.
"""
import requests
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]

    URL = "https://api.github.com/user"
    response = requests.get(URL, auth=(username, password))
    json_response = response.json()

    print(json_response.get('id'))
