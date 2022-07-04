#!/usr/bin/python3
"""3-is_kind_of_class check the same class or inheres """


def is_kind_of_class(obj, a_class):
    """
    My function is_kind_of_class: check the instance of the object
    Args:
        first parameter:obj
        second parameter: a_class
    Return:
        a boolean value after check is instantiation
    """
    if isinstance(type(obj), a_class):
        return True
    else:
        return False
