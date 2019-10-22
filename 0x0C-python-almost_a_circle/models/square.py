#!/usr/bin/python3
"""
Module square.py
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization"""
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        """recognizes the size of the square"""
        self.width = value
        self.height = value

    def __str__(self):
        """string representation"""
        return("[Square] ({}) {}/{} - {}"
               .format(self.id, self.x, self.y, self.size))

    def update(self, *args, **kwargs):
        list_upd = ["id", "size", "x", "y"]
        if args:
            count = 0
            for i in args:
                setattr(self, list_upd[count], i)
                count += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns a dictionary"""
        return({"id": self.id, "size": self.size, "x": self.x, "y": self.y})
