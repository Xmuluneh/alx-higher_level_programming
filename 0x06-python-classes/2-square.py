#!/usr/bin/python3
"""A class Square that defined based on 1-quare.py """


class Square:
    """ Square class with a private attribute"""

    def __init__(self, size=0):

        """Initialize the size variable
        Args:
            __size(int):set the new size value
            """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
