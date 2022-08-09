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

    @property
    def width(self):
        """Retrieve of private attribute width"""
        return self.__width
    
    @width.setter
    def width(self, width):
        """Set the value of __width

        Args:
            width (int): new width of square.
        """
        if (type(width) is not int):
            raise TypeError("size must be an integer")
        if width < 0:
            raise ValueError("size must be >= 0")
        self.__width = width

    
    @property
    def height(self):
        """Retrieve of private attribute height"""
        return self.__height
    
    @height.setter
    def height(self, height):
        """Set the value of __height

        Args:
            height (int): new height of square.
        """
        if (type(height) is not int):
            raise TypeError("size must be an integer")
        if height < 0:
            raise ValueError("size must be >= 0")
        self.__height = height
