#!/usr/bin/python3
"""Module 6-load_from_json_file
   Create an object from JSON file
"""
import json as j


def load_from_json_file(filename):
    """Create an Object from jsonfile
       Args:
           -filename:name of the file

    """
    with open(filename, 'r') as f:
        j.load(f)
