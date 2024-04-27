#!/usr/bin/python3
"""
This script takes a letter as input and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter. If no argument is given, it sets q="".
"""

import requests
import sys

if __name__ == '__main__':
    URL = 'http://0.0.0.0:5000/search_user'
    letter = sys.argv[1] if len(sys.argv) > 1 else ""

    response = requests.post(URL, data={'q': letter})

    if response.headers['content-type'] == 'application/json':
        result = response.json()
        if result:
            print("[{}] {}".format(result['id'], result['name']))
        else:
            print("No result")
    else:
        print("Not a valid JSON")
