#!/usr/bin/python3
""" Define rectangle based on 8-rectangle.py """


class Rectangle:
    """define the rectangle class """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):

        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """property to retrieve the width """
        return self.__width

    @width.setter
    def width(self, value):
        """property setter ,for setting width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Property to retrieve ethe height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Property setter, for setting height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """My function area
        Return:
            the area of the rectangle
            """
        return self.__width * self.__height

    def perimeter(self):
        """My function perimeter
        Return:
            the perimeter of the rectangle
            """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the string representation of rectangle with # character"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectange_list = []
        for i in range(self.__height):
            [rectange_list.append(str(self.print_symbol)) for k in range(self.__width)]
            if i != self.__height - 1:
                rectange_list.append("\n")
        return "".join(rectange_list)

    def __repr__(self):
        """Return the string representation of the rectangle"""
        rectangle = "Rectangle(" + str(self.__width)
        rectangle += ", " + str(self.__height) + ")"
        return rectangle

    def __del__(self):
        """Delete the rectangle objet before the garbage collector
        destroy the object
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """My  static function bigger_or_equal:
         compare the both Rectangle objects based on its area
        Args:
            rect_1 :the first object
            rect_2:the second object
        Return :
              the biggest rectangle based in the area
            """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """My class function square
          Args:
              size the new parameter for the class
          Return :
                the class instance size
        """
        return cls(size, size)
