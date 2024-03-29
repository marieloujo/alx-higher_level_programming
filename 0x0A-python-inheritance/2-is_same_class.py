#!/usr/bin/python3
""" Module 2-is_same_class - contains is_same_class function
"""


def is_same_class(obj, a_class):
    """ True if the object is exactly an instance of the specified class
    otherwise False
    """
    return type(obj) == a_class
