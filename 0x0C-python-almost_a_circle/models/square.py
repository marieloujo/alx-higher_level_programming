#!/usr/bin/python3
""" Module sqhare
Rectangle = __import__('rectangle').Rectangle
from models.rectangle import Rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """A representation of a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes the square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """informal string representation of the square"""
        return "[Square] ({s.id}) {s.x}/{s.y} - {s.width}".format(self=self)
