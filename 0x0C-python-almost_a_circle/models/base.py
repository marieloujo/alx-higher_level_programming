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

    @classmethod
    def save_to_file(cls, list_objs):
        """ JSON string representation of list_objs to a file """
        list_objs_json = []
        fileneme = cls.__name__ + ".json"
        if list_objs is not None:
            for obj in list_objs:
                list_objs_json.append(obj.to_dictionary())
        with open(fileneme, 'w', 'utf-8') as f:
            f.write(cls.to_json_string(list_objs_json))
