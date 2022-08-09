#!/usr/bin/python3
"""
    Module 0-rectangle - contain definition
    of class rectangle
"""


class Rectangle:
    """Defines an empty class Rectangle

        Attributes:
            __width (int): private attr, contain value of rectangle width
            __height (int): private attr, contain value of rectangle height

    """

    def __init__(self, width=0, height=0):
        """Class constructeur

        Args:
            width (int): passed value of rectangle width
            height (int): passed value of rectangle height
        """
        self.height = height
        self.width = width

    def area(self):
        """Return the area of rectangle based
        on its width and height
        """
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of rectangele based
        on its width and height
        """
        return (self.width + self.height) * 2

    @property
    def width(self):
        """Retrieve of private attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the value of __width

        Args:
            value (int): new width of square.
        """
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve of private attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the value of __height

        Args:
            value (int): new height of square.
        """
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
