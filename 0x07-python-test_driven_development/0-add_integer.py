#!/usr/bin/python3
"""  My function: add_integer
                  Adds two integers
    Return:
         Sum of two integers
"""


def add_integer(a, b=98):
    """ a-the first integer
        b-the second integer argument 98.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
