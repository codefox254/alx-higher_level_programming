#!/usr/bin/python3
"""
This script takes a URL as input, sends a GET request to the URL using the requests library, and displays the value of the X-Request-Id variable in the response header.
"""
from requests import get
from sys import argv

if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: {} <URL>".format(argv[0]))
        exit(1)

    response = get(argv[1])
    x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id if x_request_id else "X-Request-Id not found")
