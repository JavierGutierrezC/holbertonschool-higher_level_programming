#!/usr/bin/python3

"""
Function that prints a square with the character #
"""


def print_square(size):

    """
    size is the size length of the square, it must be an integer
    and it must be larger than 0; If not rise a TypeError
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for x in range(size):
        for y in range(size):
            print("#", end="")
        print()
