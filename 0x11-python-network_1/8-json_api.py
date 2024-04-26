#!/usr/bin/python3
"""
This script takes a letter as input and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter. If no argument is given, it sets q="".
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    url = "http://0.0.0.0:5000/search_user"
    payload = {'q': letter}

    response = requests.post(url, data=payload)

    try:
        json_response = response.json()
        if json_response:
            print("[{}] {}".format(json_response.get('id'), json_response.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
