#!/usr/bin/python3
"""A class square is defined based on 1-square.py"""


class Square:
    """ A square class with private attribute size"""

    def __int__(self, size=0):
        """Initialize the size variable"""
        self.__size = size

    def set_size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
