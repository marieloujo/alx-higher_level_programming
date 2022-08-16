#!/usr/bin/python3
""" 9-rectangle - contains definition of class Rectangle """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class Rectangle inherits fom BaseGeometry """

    def __init__(self, width, height):
        """instantiation of the rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Return the area of rectangle """
        return self.__height * self.__width

    def __str__(self):
        """ Returns a string representation of the rectangle """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
