#!/usr/bin/python3
"""
This script takes a URL as input and displays the value of the X-Request-Id variable in the response header.
"""

if __name__ == "__main__":
    import sys
    import urllib.request

    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers["X-Request-Id"])