#!/usr/bin/python3
"""Module 0-read_file.
Read from a file and print
"""


def read_file(filename=""):
    """Reads from filename and prints its content to stdout
    Args:
        first parameter: filename name of the file

     """
    with open(filename) as f:
        read_text = f.read()
        print(read_text, end="")

