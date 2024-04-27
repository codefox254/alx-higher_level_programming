#!/usr/bin/python3
"""
This script fetches the status from https://alx-intranet.hbtn.io/status using the requests library and displays the body response. 
It also handles HTTP errors.
"""

import requests

if __name__ == "__main__":
    try:
        r = requests.get('https://alx-intranet.hbtn.io/status')
        r.raise_for_status()  # Raise an HTTPError for bad status codes
        t = r.text
        print('Body response:')
        print('\t- type: {}'.format(type(t)))
        print('\t- content: {}'.format(t))
    except requests.HTTPError as e:
        print('Error code:', e.response.status_code)
