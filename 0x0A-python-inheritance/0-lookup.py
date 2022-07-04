#!/usr/bin/pyhtin3
"""MY fuction lookup returns the list of the attributes and methodoa any object """
def lookup(obj):
    """Args:
           obj
        Return:
               a list of the attribute
      """
    return dir(obj)
