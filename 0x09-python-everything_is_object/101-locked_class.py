#!/usr/bin/python3
"""Define a locked class"""


class LockedClass:
    """Prevent the user from instantiating a new lockedClass attribute
        for anything but attribute called 'first_name
    """
    __slots__ = ['first_name']
