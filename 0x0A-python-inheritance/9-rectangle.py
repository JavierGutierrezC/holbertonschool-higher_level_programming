#!/usr/bin/python3
"""
CLass based on task 6
"""


class BaseGeometry:
    """
    Geometry
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater tahn 0".format(name))


class Rectangle(BaseGeometry):
    """
    Rectangle
    """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return("[Rectangle] {}/{}".format(self.__width, self.__height))