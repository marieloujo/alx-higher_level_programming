#!/usr/bin/python3
""" Module 9-student.py """


class Student:
    """ Definition of class Student """

    def __init__(self, first_name, last_name, age):
        """ Create new instance """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation of a Student instance """
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for attr in attrs:
            try:
                new_dict[attr] = self.__dict__[attr]
            except BaseException:
                pass
        return new_dict

    def reload_from_json(self, json):
        """  Replaces all attributes of the Student instance """
        for key, value in json.items():
            try:
                setattr(self, key, value)
            except BaseException:
                pass
