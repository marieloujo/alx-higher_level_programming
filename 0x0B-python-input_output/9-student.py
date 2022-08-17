#!/usr/bin/python3
""" Module 9-student.py """


class Student:
    """ Definition of class Student """

    def __init__(self, first_name, last_name, age):
        """ Create new instance """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Retrieves a dictionary representation of a Student instance """
        return self.__dict__
