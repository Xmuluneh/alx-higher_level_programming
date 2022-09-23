#!/usr/bin/python3
"""Takes in Github credentials (username and password) and uses the Github API
to display an id
"""
if __name__ == '__main__':
    import requests
    import sys
    rul = requests.get('https://api.github.com/user',
                       auth=(sys.argv[1], sys.argv[2]))
    if rul.status_code >= 400:
        print('None')
    else:
        print(rul.json().get('id'))
