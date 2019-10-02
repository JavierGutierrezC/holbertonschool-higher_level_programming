#!/usr/bin/python3

"""Write a class Square that defines a square
uing a getter and a setter"""


class Square:

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return(self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must de >= 0")
        self.__size = value

    def area(self):
        return(self.__size * self.__size)

    def __ld__(self, other):
        return(self.area() < other.area())

    def __led__(self, other):
        return(self.area() <= other.area())

    def __et__(self, other):
        return(self.area() == other.area())

    def __dif__(self, other):
        return(self.area() != other.area())

    def __gd__(self, other):
        return(self.area() > other.area())

    def __ged__(self, other):
        return(self.area() >= other.area())
