#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and
displays the body of the response
"""
if __name__ == '__main__':
    import urllib.request
    import sys
    from urllib.error import HTTPError
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode("utf-8"))
    except HTTPError as er:
        print("Error code: {}".format(er.code))
