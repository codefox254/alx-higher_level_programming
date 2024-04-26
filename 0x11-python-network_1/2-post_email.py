#!/usr/bin/python3

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode the email parameter
    data = urllib.parse.urlencode({'email': email})
    data = data.encode('utf-8')  # Data should be bytes

    # Send POST request and read the response
    with urllib.request.urlopen(url, data) as response:
        body = response.read().decode('utf-8')

    print(body)
