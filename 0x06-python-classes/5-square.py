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
        self.size = size

    @property
    def size(self):
        """Retrieve of private attribute size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the value of __size

        Args:
            param1 (value: int): new value of square.
            It must be an int and gretter than or equal 0.
        """

        if (type(value) is not int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Public instance method: compute the area of square

        Returns:
            Int: value of area
        """
        return self.__size * self.__size

    def my_print(self):
        """my_print - print square with '#' if empty size nothing is print"""
        for row in range(self.size):
            for iem in range(self.size):
                print("#", end="")
            print()
        if self.size is 0:
            print()
