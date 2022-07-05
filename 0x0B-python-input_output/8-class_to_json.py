#!/usr/bin/python3
"""Module 8-class_to_json
  Returns the dictionary description with simple
  data structure (list, dictionary, string, integer and boolean)
  for JSON serialization of an object
"""


def class_to_json(obj):
    """Create a dictionary description of object
       Args:
           -obj:Object to serialize
       Return:
           -dictionary description of object

    """
    return obj.__dict__
