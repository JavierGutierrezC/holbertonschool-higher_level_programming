#!/usr/bin/python3
"""
function that returns True if the object is exactly an
instance of the specified class ; otherwise False
"""


def is_same_class(obj, a_class):
    """
    Returns true if it is an instance of the class otherwise false
    """
    if type(obj) is a_class:
        return True
    return False
