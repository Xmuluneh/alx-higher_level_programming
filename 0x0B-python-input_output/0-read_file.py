#!/usr/bin/python3
"""Module 0-read_file.
Read from a file and print
"""


def read_file(filename=""):
    """MY function read_file: read text from file and print its content on the stdout
    Args:
        first parameter: filename string

     """
    with open(filename, encoding="utf-8") as f:
        read_text = f.read()
        print(read_text, end="")
    f.close()
