#!/usr/bin/python3
class Square:
    """Represents a square.
    Private instance attribute: size.
    Instantiation with optional size.
    """

    def __init__(self, size=0):

        """Initialize the size variable"""
        self.setSize(size)

    def setSize(self, size):

        """set the Initializes data."""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

