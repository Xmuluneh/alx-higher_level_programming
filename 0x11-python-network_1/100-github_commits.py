#!/usr/bin/python3
"""Takes in Github repo nd owner name to list
10 commits (from the most recent to oldest)"""

if __name__ == "__main__":
    import requests
    import sys

    repo = sys.argv[1]
    owner = sys.argv[2]

    response = requests.get(
            "https://api.github.com/repos/{}/{}/commits"
            .format(owner, repo))

    auth_json = response.json()

    for comm in auth_json[:10]:
        print("{}: {}".format(
            comm.get("sha"),
            comm.get("commit")
            .get("author")
            .get("name")))
