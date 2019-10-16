#!/usr/bin/python3
"""
function that returns if the object is an instance of a class that inherited
from the specified class
"""


def inherits_from(obj, a_class):
    """
    True if instance else False
    """
    if type(obj) is a_class:
        return False
    elif issubclass(type(obj), a_class):
        return True
