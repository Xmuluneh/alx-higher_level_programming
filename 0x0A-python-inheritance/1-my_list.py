#!/usr/bin/python3
"""MyList class inherited from list"""


class MyList(list):
    """A class MyList inherited from list"""
    def print_sorted(self):
        """MY print_sorted function print the given list in ascending order"""
        return print(sorted(self))
