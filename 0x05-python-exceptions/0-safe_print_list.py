#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """The function print the elements of the list using try/exception"""
    element_count = 0
    for i in range(x):
        try:
            print('{:d}'.format(i))
            element_count += 1
        except IndexError:
            print("Sorry invalid index")
    print()
    return element_count
