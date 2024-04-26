#!/usr/bin/python3
"""
This script takes a URL as input, sends a request to the URL, and displays the body of the response. It handles HTTP errors using urllib.error.HTTPError.
"""

if __name__ == '__main__':
    import sys
    from urllib import request, error

    argv = sys.argv
    url = argv[1]
    try:
        with request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as err:
        print("Error code: {}".format(err.status))