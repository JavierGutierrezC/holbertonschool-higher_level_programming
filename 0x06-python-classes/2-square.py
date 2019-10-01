#!/usr/bin/python3

"""Write a class Square that defines a square"""


class Square:

    """Initialize with size. rise TypeError if conditions not met"""

    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
