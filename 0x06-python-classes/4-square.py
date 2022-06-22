#!/usr/bin/python3
"""The class is defined based on 3-square.py"""


class Square:
    def __init__(self, size=0):
        """Initialize the size value
        Args:
            size: the size of a square is initialized
            """
        self.__size = size

    @property
    def size(self):
        """Return the optimal value of size
        Args:
            size : The size of a square
            """
        return self.__size

    @size.setter
    def size(self, value):
        """Set a new value for size if the conditions are passed.
         Args:
             size:set a new value for size
             """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculate the area of the square and return value """
        return self.__size ** 2