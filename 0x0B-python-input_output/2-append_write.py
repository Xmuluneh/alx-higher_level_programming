#!/usr/bin/python3
"""Module 2-append_write.
   Append a string at the end of a  text file
"""


def append_write(filename="", text=""):
    """Appends a text file
        Args:
            -filename:name of the file
            -text:string append in the file
        Return :number of character append

    """
    with open(filename, 'a+') as f:
        return f.write(text)
