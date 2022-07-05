#!/usr/bin/python3
class Student:
    """ Class:Student

    """

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
        """the functon to_json return the dictionary
        representation of the clas Strident
        """

        return self.__dict__
