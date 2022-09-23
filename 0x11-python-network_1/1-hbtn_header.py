#!/usr/bin/python3
if __name__ == 'main':
    import urllib.request
    import sys
    with urllib.request.urlopen(sys.argv[1]) as response:
        head = response.headers.get('X-Request-Id')
