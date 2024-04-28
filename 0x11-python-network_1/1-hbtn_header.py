#!/usr/bin/python3
"""
This script takes a URL as input and displays the value of the X-Request-Id variable in the response header.
"""
import sys
import urllib.request

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            x_request_id = response.headers.get("X-Request-Id")
            if x_request_id:
                print(x_request_id)
            else:
                print("X-Request-Id not found in the response header.")
    except Exception as e:
        print("An error occurred:", e)
