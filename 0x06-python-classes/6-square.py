#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """An Square class

    Attributes:
        attr1 (__size: int): Private instance attribute, size of obj od square
    """

    def __init__(self, size=0, position=(0, 0)):
        """The constructor of class

        Args:
            param1 (size: int): initialize value to size.

        Returns:
            None
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieve of private attribute position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the value of __position

        Args:
            param1 (value: tuple): new value of square.
        """

        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Public instance method: compute the area of square

        Returns:
            Int: value of area
        """
        return self.__size * self.__size

    def my_print(self):
        """my_print - print square with '#' if empty size nothing is print"""
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            print("".join([" " for sp in range(self.__position[0])]), end="")
            print("".join(["#" for tag in range(self.__size)]))
        if self.size is 0:
            print()
