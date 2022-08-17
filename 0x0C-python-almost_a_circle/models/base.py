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
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ JSON string representation of list_objs to a file """
        filename = cls.__name__ + ".json"
        list_objs_json = []
        if list_objs is not None:
            for i in list_objs:
                list_objs_json.append(cls.to_dictionary(i))
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(list_objs_json))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set """
        if cls.__name__ is "Rectangle":
            obj = cls(1, 1)
        elif cls.__name__ is "Square":
            obj = cls(1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        objects = []
        try:
            with open(filename, 'r') as f:
                objects = cls.from_json_string(f.read())
            for i in range(len(objects)):
                objects[i] = cls.create(**objects[i])
        except BaseException:
            pass
        return objects
