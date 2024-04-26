#!/usr/bin/python3
"""
This script takes a URL as input, sends a GET request to the URL using the requests library, and displays the body of the response. If the HTTP status code is greater than or equal to 400, it prints an error message containing the status code.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)

    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
