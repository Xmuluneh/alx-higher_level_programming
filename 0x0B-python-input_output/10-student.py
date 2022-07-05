#!/usr/bin/python3
"""Module 10-student (based on 9-student.py)
   class:Student
"""


class Student:

    def __init__(self, first_name, last_name, age):
        """initialise the parameter list
            Args:
                -first par.: first_name
                - Second par.:last_name
                -third par.:age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of
           class
        """
        my_dict = dict()
        if type(attrs) is list and all(type(x) is str for x in attrs):
            for x in attrs:
                if x in self.__dict__:
                    my_dict.update({x: self.__dict__[x]})
            return my_dict
        return self.__dict__.copy()
