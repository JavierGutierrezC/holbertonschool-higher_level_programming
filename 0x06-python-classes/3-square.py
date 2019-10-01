#!/usr/bin/python3

"""Write a class that defines a square
private instance size.
Initiate with size"""

class Square:

    """Size must be an integer or bigger than 0, if not raise error.
    Use public instace method to return current area"""
    def __init__(self, size = 0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")


    def area(self):
        return(self.__size * self.__size)
