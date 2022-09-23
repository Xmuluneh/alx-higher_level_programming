#!/usr/bin/python3
""" A module to find the maximum element in the list """


def find_peak(list_of_integers):
    """Find the peck element in the list"""
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if list_of_integers is None or list_of_integers == []:
        return None
    else:
        num = list_of_integers[0]
        for i in list_of_integers:
            if i > num:
                num = i
        return num
