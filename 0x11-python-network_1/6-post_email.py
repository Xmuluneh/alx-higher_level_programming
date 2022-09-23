#!/usr/bin/python3
"""Takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response
"""
if __name__ == '__main__':
    import requests as r
    import sys
    rul = r.post(sys.argv[1], date={'email': sys.argv[2]})
    print(rul.txt)
