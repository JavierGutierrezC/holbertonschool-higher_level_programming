#!/usr/bin/python3
"""
function that returns if the object is an instance of a class that inherited
from the specified class
"""


def inherits_from(obj, a_class):
    """
    True if instance else False
    """
    if issubclass(type(obj), a_class) and a_class is not type(obj):
        return(True)
    else:
        return(False)
