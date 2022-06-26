#!/usr/bin/python3
""" add_integer
    Adds two integers
"""


def add_integer(a, b=98):
    """add function add two integers
    Args: a-the first integer
          b-the second integer argument 98.
    Return : Sum of two integer
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
