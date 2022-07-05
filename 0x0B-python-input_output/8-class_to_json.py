#!/usr/bin/python3
"""Module 8-class_to_json
   JSON serialization of an object
"""
import json as j


def class_to_json(obj):
    """Create a dictionary description of object
       Args:
           -obj:Object to serialize
       Return:
           -dictionary description of object

    """
    return obj.__dict__
