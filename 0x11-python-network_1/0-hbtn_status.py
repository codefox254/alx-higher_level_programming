#!/usr/bin/python3
"""
This script fetches the status from https://alx-intranet.hbtn.io/status 
and displays the body response.
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