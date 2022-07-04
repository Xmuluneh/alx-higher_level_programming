#!/usr/bin/python3
"""2-is_same_class checking the instance of the given object"""


def is_same_class(obj, a_class):
    """MY function is_same_class check the instance of the object
    Args:
        the first parameter any object
        the second parameter is a_class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
