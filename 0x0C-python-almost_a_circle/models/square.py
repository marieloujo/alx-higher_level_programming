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
        self.size = size

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value

    def __str__(self):
        """informal string representation of the square"""
        return "[Square] ({s.id}) {s.x}/{s.y} - {s.width}".format(s=self)

    def update(self, *args, **kwargs):
        """ Update the class Square """
        if (args):
            arguments = {0: 'id', 1: 'size', 2: 'x', 3: 'y'}
            for i in range(len(args)):
                setattr(self, arguments[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of a Square """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
