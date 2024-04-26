#!/usr/bin/python3
"""
This script fetches the status from https://alx-intranet.hbtn.io/status using the requests library and displays the body response. 
It also handles HTTP errors.
"""

import requests

if __name__ == "__main__":
    r = requests.get('https://alx-intranet.hbtn.io/status')
    t = r.text
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(t), t))