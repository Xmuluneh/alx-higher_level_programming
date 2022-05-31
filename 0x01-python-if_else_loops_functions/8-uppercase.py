#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        letter = ord(str[i])
        if 97 <= letter < 123:
            letter = letter - 32
        print("{}".format(chr(letter)), end='')
    print()
