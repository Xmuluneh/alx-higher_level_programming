#!/usr/bin/python3
def safe_print_division(a, b):
    """The function do the safe division of numbers"""
    try:
        num = a / b

    except (TypeError, ZeroDivisionError):
        num = None
    finally:
        print("{}".format(num))
    return num
