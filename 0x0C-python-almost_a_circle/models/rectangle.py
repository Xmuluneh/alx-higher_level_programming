#!/usr/bin/python3
"""Module Rectangle inherited from Base"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle with private instance
       Inherited from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle instance

           Args:
               -__width : width
               -__height : height
               -__x: position
               -__y:position
               -id:id

        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def height(self):
        """Retrieve the attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def width(self):
        """Retrieve the attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def x(self):
        """Retrieve the attribute x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the attribute x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrieve the y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the attribute y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate the area of the Rectangle instance
           Return: area
        """
        return self.__width * self.__height

    def display(self):
        """Print in stdout the  Rectangle instance with the # character"""
        print("\n" * self.y, end="")
        print((" " * self.x + "#" * self.__width + '\n') * self.__height, end="")

    def __str__(self):
        """Return the string representation of a Rectangle instance"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """update attribute of an instance
           Args:
               -id attribute
               -width attribute
               -height attribute
               -x attribute
               -y attribute

        """
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle."""

        return {'id': self.id, 'width': self.__width, 'height': self.__height, 'x': self.__x, 'y': self.__y}
