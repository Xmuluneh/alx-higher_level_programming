#!/usr/bin/python3
"""3-is_kind_of_class check the instance of the object to the given call or inheres """


def is_kind_of_class(obj, a_class):
    """
    My function is_kind_of_class: check the instance of the object
    Args:
        first parameter:obj
        second parameter: a_class
    Return:
        a boolean value after check is instantiation
    """
    return True if isinstance(type(obj), a_class) else False
