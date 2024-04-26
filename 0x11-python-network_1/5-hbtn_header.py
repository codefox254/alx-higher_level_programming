#!/usr/bin/python3
"""
This script takes a URL as input, sends a GET request to the URL using the requests library, and displays the value of the X-Request-Id variable in the response header.
"""

if __name__ == '__main__':
    from requests import get
    from sys import argv

    res = get(argv[1])
    print(res.headers.get('X-Request-Id'))