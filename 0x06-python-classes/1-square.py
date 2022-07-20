#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """An Square class
        Attributes:
            attr1 (__size): Private instance attribute, size of obj od square
    """

    def __init__(self, size):
        """The constructor of class
            Args:
                param1 (size): initialize value to size.
        """
        self.__size = size
