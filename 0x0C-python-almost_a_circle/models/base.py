#!/usr/bin/python3
"""module Base"""

import json
import os
import csv


class Base:
    """class with private attribute
        __nb_objects
     """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the Base class instance
        Args:
            -id:id of the instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """The Json object as string representation of list_dictionaries
           Args:
               -list_dictionaries
           Return :
                   Json representation of alist
         """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if type(list_dictionaries) is not list or not all(type(x) == dict for x in list_dictionaries):
            raise TypeError("list_dictionaries must be a list of dictionary ")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Serializing list_objs in csv form and save to file
        Args:
            -list_objs : list instance
        """
        if type(list_objs) is not list and list_objs is not None or not all(isinstance(x, cls) for x in list_objs):
            raise TypeError("list_objs must be a list instance")
        if list_objs is None:
            with open(cls.__name__ + ".json", "w") as file:
                file.write("[]")
        else:
            list_instance = [i.to_dictionary() for i in list_objs]
            with open(cls.__name__ + ".json", "w") as file:
                file.write(cls.to_json_string(list_instance))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string
        representation json_string

        Args:
            json_string(str): a string representing a list
            of dictionaries

        """
        if json_string is None:
            return []
        if json_string == [] or not isinstance(json_string, str):
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set

        Args:
            **dictionary(pointer): can be thought of as a
            double pointer to a dictionary

        """
        if cls.__name__ == "Rectangle":
            result = cls(32, 3)
            result.update(**dictionary)
            return result
        if cls.__name__ == "Square":
            result = cls(32)
            result.update(**dictionary)
            return result

    @classmethod
    def load_from_file(cls):

        list_instance = []
        file_name = cls.__name__ + ".json"
        if os.path.isfile(file_name):
            with open(file_name, "r") as file:
                s = cls.from_json_string(file.read())
            for i in s:
                list_instance.append(cls.create(**i))
            return list_instance
        return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """A  class method that serializes and
           deserializes in CSV

        """
        if (list_objs is None or not isinstance(list_objs, list) or not all(isinstance(j, Base) for j in list_objs)):
            with open(cls.__name__ + ".csv", "w") as f:
                f.write("[]")
        if list_objs and any(isinstance(j, Base) for j in list_objs):
            dict_data = [i.to_dictionary() for i in list_objs]
            if cls.__name__ == "Rectangle":
                csv_columns = ["id", "width", "height", "x", "y"]
            else:
                csv_columns = ["id", "size", "x", "y"]
            with open(cls.__name__ + ".csv", "w") as file:
                writer = csv.DictWriter(file, fieldnames=csv_columns)
                writer.writeheader()
                for data in dict_data:
                    writer.writerow(data)

    @classmethod
    def load_from_file_csv(cls):
        """Loads from csv file"""
        list_instance = []
        name = cls.__name__ + ".csv"
        if os.path.isfile(name):
            with open(name, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    d = {key: int(value) for key, value in row.items()}
                    list_instance.append(cls.create(**d))
            return list_instance
        return []
