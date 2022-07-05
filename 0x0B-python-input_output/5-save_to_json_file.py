#!/usr/bin/python3
"""Module 5-save_to_json_file
   Write an object to the text file using JSon representation
"""
import json as j


def save_to_json_file(my_obj, filename):
    """Writer the representation of my_obj to a filename
      Args:
          -my_obj: object to write
          -filename: file to write in to
    """
    with open(filename,'w+') as f:
        j.dump(my_obj, f)
