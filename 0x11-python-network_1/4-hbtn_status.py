#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status"""


if __name__ == '__main__':
    import requests as r
    rul = r.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(rul.text)))
    print('\t- content: {}'.format(rul.text))
