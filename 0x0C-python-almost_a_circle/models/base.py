#!/usr/bin/python3
"""module Base"""


class Base:
    """class with private attribute
        __nb_objects
     """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the Base class instance
        Args:
            -id:id of the instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
