#!/usr/bin/python3
"""Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
if __name__ == '__main__':
    import requests as r
    import sys
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    rul = r.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        dic_value = rul.json()
        if dic_value == {}:
            print("No result")
        else:
            print("[{}] {}".format(dic_value.get('id'), dic_value.get('name')))
    except ValueError:
        print('Not a valid Json')
