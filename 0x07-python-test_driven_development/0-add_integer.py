#!/usr/bin/python3

"""
Function that adds two integers(a,b)
Both have to be float numbers
Return sum of both
"""


def add_integer(a, b=98):

    """
    Receive two numbers (a, b), if not a TypeError must be raised
    """

    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return int(a) + int(b)
    elif not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
