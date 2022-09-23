#!/usr/bin/python3
"""Takes in Github repo nd owner name to list
10 commits (from the most recent to oldest)"""
if __name__ == '__main__':
    import requests as r
    import sys

    rul = r.get('https:api.github.com/repos/{}/{}/commits'.
                format(sys.argv[2], sys.argv[1]))
    if rul.status_code >= 400:
        print('None')
    else:
        for commit in rul.json[:10]:
            print('{}: {}'.format(commit.get('sha'), commit.get('commit').
                                  get('author').get('name')))
