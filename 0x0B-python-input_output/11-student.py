#!/usr/bin/python3
"""Module 11-student based on 10-student.py
  Class Student
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
        """Retrieves a dictionary representation
        of a Student instance.

        """

        my_dict = dict()
        if attrs and all(isinstance(x, str) for x in attrs):
            for x in attrs:
                if x in self.__dict__:
                    my_dict.update({x: self.__dict__[x]})
            return my_dict
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance.
        Args:
            - json: dictionary of attributes
        """

        for x in json:
            self.__dict__.update({x: json[x]})
