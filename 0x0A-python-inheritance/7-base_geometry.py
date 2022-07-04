#!/usr/bin/python3
"""A class BaseGeometry based on 6-base_geometry.py"""


class BaseGeometry:
    def area(self):
        """My function area : with no parameter"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """My function integer_validator: validate the value
            Args:
                first parameter : name str
                second parameter :value int
            Return value
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return value
