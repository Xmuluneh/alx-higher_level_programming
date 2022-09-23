#!/usr/bin/python3
""""Takes in a URL, sends a request to the URL and
displays the body of the response
"""
if __name__ == '__main__':
    import requests as r
    import sys
    rul = r.get(sys.argv[1])
    if rul.status_code >= 400:
        print("Error code: {}".format(rul.status_code))
    else:
        print(rul.text)
