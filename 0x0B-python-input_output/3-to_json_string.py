#!/usr/bin/python3
"""Module 3-to-json_string.
   Return the JSON representation of object
"""

import json as j


def to_json_string(my_obj):
    """ RReturn the JSON representation of my_obj
       Args:
           -my_obj: name of the object
       Return:
           -json representation of the object

    """
    return j.dumps(my_obj)
