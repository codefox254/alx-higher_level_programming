#!/usr/bin/python3

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
