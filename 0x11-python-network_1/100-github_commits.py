#!/usr/bin/python3
"""
This script lists 10 commits (from the most recent to oldest) of the repository specified by the user and owner names using the GitHub API.
"""

import requests
import sys

if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]
    i = 0

    URL = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)

    response = requests.get(URL)
    commits = response.json()

    for commit in commits[:10]:
        sha = commit.get('sha')
        author = commit.get('commit').get('author').get('name')
        print("{}: {}".format(sha, author))
