#!/usr/bin/python3
"""Module 9-student
       Class:Student
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

    def to_json(self):
        """Retrieves a dictionary representation
        of a Student instance.
        Returns: the dict representation of the instance.
        """
        return self.__dict__
