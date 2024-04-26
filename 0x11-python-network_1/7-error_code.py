#!/usr/bin/python3
"""
This script takes a URL as input, sends a GET request to the URL using the requests library, and displays the body of the response. If the HTTP status code is greater than or equal to 400, it prints an error message containing the status code.
"""

if __name__ == '__main__':
    from sys import argv
    from requests import get

    url = argv[1]

    response = get(url)
    ERR_TXT = 'Error code: {}'
    status = response.status_code
    print(ERR_TXT.format(status) if (status >= 400) else response.text)