#!/usr/bin/python3

"""
Function that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):

    """
    first_name and last_name must be strings
    if not raise a TypeError
    """
    if isinstance(first_name, str) and isinstance(last_name, str):
        print("My name is {} {}".format(first_name, last_name))
    elif not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
