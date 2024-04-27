#!/usr/bin/python3
"""
This script takes a URL and an email address as input, 
sends a POST request to the URL with the email as a parameter, and displays the body of the response.
"""

import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({"email": email}).encode('ascii')

    try:
        with urllib.request.urlopen(url, data) as response:
            print("Email:", email)
            print(response.read().decode('utf-8'))
    except Exception as e:
        print("An error occurred:", e)
