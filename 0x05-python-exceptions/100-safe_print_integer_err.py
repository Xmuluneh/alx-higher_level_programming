#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """The function do prnt integer values and retuen True """
    try:
        print("{:d}".format(value))
        num = True
    except:
        print("Exception:", sys.exc_info()[1], file=sys.stderr)
        num = False
    return num
