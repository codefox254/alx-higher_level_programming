#!/usr/bin/python3
"""
This script fetches the status from https://alx-intranet.hbtn.io/status and displays the body response.
"""

import urllib.request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as response:
        body = response.read().decode('utf-8')

    print("- Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
