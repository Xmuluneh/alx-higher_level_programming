#!/usr/bin/python3
"""A class square is defined based on 1-square.py"""


class Square:
    """ A square class with private attribute size"""
    def __int__(self, size=0):
        """Initialize the size variable"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        else:
            raise ValueError("size must be >= 0")
