#!/usr/bin/python3

"""
Function that prints a text afer a new line
after each character., ?, :
"""


def text_indentation(text):

    """
    Raise a TypeError if text is not a string
    No spaces atthe beginning or end of each printed line
    Return text with spaces
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    tc = text.replace(". ",".").replace("? ","?").replace(": ",":")
    nt = tc.replace(".", ".\n\n").replace("?", "?\n\n").replace(":", ":\n\n")
    print(nt, end="")
