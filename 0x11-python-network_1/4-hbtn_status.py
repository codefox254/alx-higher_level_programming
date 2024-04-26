#!/usr/bin/python3

"""
This script fetches the status from https://alx-intranet.hbtn.io/status using the requests library and displays the body response. It also handles HTTP errors.
"""

import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    response = requests.get(url)

    if response.status_code == 200:
        print("- Body response:")
        print("\t- type:", type(response.text))
        print("\t- content:", response.text)
    else:
        print(f"Error code: {response.status_code}")
