#!/usr/bin/python3
"""module rectangle.py"""
from models.base import Base


class Rectangle(Base):
    """class rectangle that inherites from base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """hight getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """hight setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """retrurns area"""
        return self.height * self.width

    def display(self):
        """prints using # character"""
        if self.width == 0:
            print("")
        for i in range(self.y):
            print("")
        for i in range(self.height):
            print(" " * self.x, end="")
            for j in range(self.width):
                print("{}".format("#"), end="")
            print("")

    def __str__(self):
        """string representaion print"""
        return("[Rectangle] ({}) {}/{} - {}/{}"
               .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """Dictionary update"""
        item_list = ["id", "width", "height", "x", "y"]
        if args:
            count = 0
            for i in args:
                setattr(self, item_list[count], i)
                count += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """dictionary representation"""
        return({"id": self.id, "width": self.width,
                "height": self.height, "x": self.x, "y": self.y})
