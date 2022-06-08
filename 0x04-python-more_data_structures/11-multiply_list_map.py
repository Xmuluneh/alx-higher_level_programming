#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """Return the square of a list without for loop"""
    return (list(map(lambda x: x * number, my_list)))
