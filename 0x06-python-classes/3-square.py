#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """An Square class

    Attributes:
        attr1 (__size: int): Private instance attribute, size of obj od square
    """

    def __init__(self, size=0):
        """The constructor of class

        Args:
            param1 (size: int): initialize value to size.

        Returns:
            None
        """

        if (type(size) is not int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Public instance method: compute the area of square

        Returns:
            Int: value of area
        """
        return self.__size * self.__size
