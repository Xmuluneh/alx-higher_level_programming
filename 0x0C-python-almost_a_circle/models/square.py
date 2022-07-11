#!/usr/bin/python3
"""Module Square
    inherited from Rectangle
"""
from . import rectangle
from . import base


class Square(rectangle.Rectangle):
    """A class Square inherited from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the square class attributes
           Args:
               -size:size
               -x:x
               -y:y
               -id:id
        """
        super().__init__(size, size, x, y, id)

        self.size = size

    def __str__(self):
        """Return the string representation of square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """Retrieve the size attribute"""
        return self.__width

    @size.setter
    def size(self, value):
        """Sets a new value for size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update attribute of an instance
           Args:
               -id attribute
               -size attribute
               -x attribute
               -y attribute
        """
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args) is not int and args[0] is None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __dec__(self):
        """Return a string representation of a square"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

    def to_dictionary(self):
        """Return the dictionary representation of the square class"""
        return {'id': self.id, 'x': self.x, 'size':self.size,'y':self.y}
