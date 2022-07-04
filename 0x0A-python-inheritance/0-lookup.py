#!/usr/bin/python3
"""MY function lookup returns the list of the attributes and method any object """


def lookup(obj):
    """Args:
           obj
        Return:
               a list of the attribute
      """
    return dir(obj)
