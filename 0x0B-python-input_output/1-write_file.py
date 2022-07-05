#!/usr/bin/python3
""" Module 1-write_file
    Write in the text file
"""


def write_file(filename="", text=""):
    """ Write text in  a file
        Args:
            -filename: name of the file
            -text : string to write in the file
        Return: number of character written


    """
    with open(filename, 'w+') as f:
        return f.write(text)
