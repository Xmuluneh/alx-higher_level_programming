#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response
"""
if __name__ == 'main':
    import urllib.request
    import sys
    with urllib.request.urlopen(sys.argv[1]) as response:
        head = response.info()
        print(head['X-Request-Id'])
