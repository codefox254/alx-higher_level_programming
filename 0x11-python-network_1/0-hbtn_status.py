#!/usr/bin/python3
"""
This script fetches the status from a specified URL and displays the body response.
"""
import sys
from urllib import request, error

if __name__ == '__main__':
    # Check if URL argument is provided
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    
    try:
        with request.urlopen(url) as response:
            body = response.read()
            print("Body response:")
            print("- type:", type(body))
            print("- content:", body)
            print("- utf8 content:", body.decode('utf-8'))
    except error.HTTPError as err:
        print("Error code:", err.code)
