#!/usr/bin/python3
"""
This script takes a URL as input, sends a GET request to the URL using the requests library, and displays the body of the response. If the HTTP status code is greater than or equal to 400, it prints an error message containing the status code.
"""

from sys import argv
from requests import get

if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: {} <URL>".format(argv[0]))
        exit(1)

    url = argv[1]

    response = get(url)
    status = response.status_code

    if status >= 400:
        print("Error code:", status)
    else:
        print(response.text)
