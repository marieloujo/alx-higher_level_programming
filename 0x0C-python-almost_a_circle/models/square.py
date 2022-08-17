#!/usr/bin/python3
""" Module sqhare
Rectangle = __import__('rectangle').Rectangle
from models.rectangle import Rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Definition of class Square """

    def __init__(self, size, x=0, y=0, id=None):
        """ Create new square """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Retrieve of private attribute __size"""
        return self.width

    @size.setter
    def size(self, value):
        """Set the value of __size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """ String representation of square """
        return "[Square] (" +\
               "{s.id}) {s.x}/{s.y} - {s.width}/{s.height}".format(s=self)
