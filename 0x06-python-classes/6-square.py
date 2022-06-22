#!/usr/bin/python3

"""A square class that prints a square size hashtags(#)"""


class Square:
    """A square class that prints a square size hashtags(#)"""

    def __init__(self, size=0, position=(0, 0)):
        """Inits Square.
        Args:
            size: size of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """A method for retriving size.
        Args:
            size: size of the sqaure
        """
        return self.__size

    @size.setter
    def size(self, size):
        """A method for setting size with exceptions
        Args:
            size: size of the square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def position(self):
        """ A method for retreving Position """

        return self.__position

    @position.setter
    def position(self, position):
        """ A method for setting position
        Attr:
            position: position of square
        """
        if type(position) == tuple and len(position) == 2:
            for i in position:
                if type(i) == int and i >= 0:
                    self.__position = position
                else:
                    raise TypeError("position must be a tuple of 2 positive\
 integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """A method for calculating area"""
        return int(self.__size ** 2)

    def my_print(self):
        """A method for printing squares"""

        if self.__size == 0:
            print()
        else:
            for y in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
