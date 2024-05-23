#!/usr/bin/python3
"""
This script takes a URL and an email address as input, sends a POST request to the URL with the email as a parameter, and displays the body of the response.
"""
from sys import argv
from requests import post

if __name__ == '__main__':
    if len(argv) != 3:
        print("Usage: {} <URL> <email>".format(argv[0]))
        exit(1)

    url = argv[1]
    email = argv[2]

    response = post(url, data={'email': email})

    if response.ok:
        print(response.text)
    else:
        print("Error:", response.text)
