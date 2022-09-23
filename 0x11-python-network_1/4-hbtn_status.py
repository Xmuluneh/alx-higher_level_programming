#!/usr/bin/python3
""""""
import requests as requests

if __name__ == '__main__':
    import requests as r
    rul = r.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type:{}'.format(type(rul)))
    print('\t- content: {}'.format(rul))
