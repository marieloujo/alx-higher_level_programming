#!/usr/bin/python3
""" Module - base """


import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ JSON string representation of list_dictionaries """
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)
