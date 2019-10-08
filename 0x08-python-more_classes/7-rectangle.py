#!/usr/bin/python3
"""
Write a class Rectangle that defines a rectangle.
Using 5-rectangle.py print a message of how many instances are left
"""


class Rectangle:
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return(self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return(self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return(self.width * self.height)

    def perimeter(self):
        if self.height == 0 or self.width == 0:
            return(0)
        else:
            return((self.height * 2) + (self.width * 2))

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return("")
        temp = []
        for x in range(self.height):
            temp.append("{}".format(self.print_symbol) * self.width)
            if x < (self.height - 1):
                temp.append('\n')
        return "".join(temp)

    def __repr__(self):
        return("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
