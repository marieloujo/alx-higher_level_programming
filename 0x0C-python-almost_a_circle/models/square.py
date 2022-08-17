#!/usr/bin/python3
""" Module sqhare """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Definition of class Square """

    def __init__(self, size, x=0, y=0, id=None):
        """ Create new square """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ String representation of square """
        return "[Square] (" +\
               "{s.id}) {s.x}/{s.y} - {s.width}/{s.height}".format(s=self)
