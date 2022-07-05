#!/usr/bin/python3
"""Module 2-append_write.
   Append in the file text
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file
        Args:
            -filename:name of the file
            -text:string append in the file
        Return :number of character append

    """
    with open(filename, ' a+') as f:
        return f.write(text)
