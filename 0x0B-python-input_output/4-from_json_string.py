#!/usr/bin/python3
"""Module 4-from_json_string
   Returns an object represented by a JSON string
"""
import json as j


def from_json_string(my_str):
    """ Return the string representation of the my_str
       Args:
           -my_str:name of the python data
       Return :
              -the python representation of the json file

    """
    return j.loads(my_str)
