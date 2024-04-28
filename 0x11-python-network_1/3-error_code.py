#!/usr/bin/python3
"""
This script takes a URL as input, sends a request to the URL, and displays the body of the response. It handles HTTP errors using urllib.error.HTTPError.
"""
import sys
from urllib import request, error

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]

    try:
        with request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as err:
        print("Error code:", err.status)
