#!/usr/bin/python3
"""
This script takes a URL and an email address as input, sends a POST request to the URL with the email as a parameter, and displays the body of the response.
"""

if __name__ == '__main__':
    from sys import argv
    from requests import post

    url = argv[1]
    email = argv[2]
    res = post(url, {'email': email})
    print(res.text)