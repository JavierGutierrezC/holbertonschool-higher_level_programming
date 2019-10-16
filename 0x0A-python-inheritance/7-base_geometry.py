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
