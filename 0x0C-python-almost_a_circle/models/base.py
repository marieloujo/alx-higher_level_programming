#!/usr/bin/python3
""" Module - base """


class Base:
    """ Definition of Base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Create a new instance """
        if id:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
