#!/usr/bin/python3
""" A rectangle class define rectangle based on 0-rectangle.py """


class Rectangle:
    """define the rectangle class """
    def __init__(self, width=0, height=0):
        """Initialize a rectangle instance
         Args:
             width(int) with a new width
             height(int) with a new height
             """
        self.width = width
        self.height = height

    @property
    def width(self):
        """property to retrieve the width """
        return self.__width

    @width.setter
    def width(self, value):
        """property setter ,for setting width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Property to retrieve the height
            """
        return self.__height

    @height.setter
    def height(self, value):
        """Property setter, for setting height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
