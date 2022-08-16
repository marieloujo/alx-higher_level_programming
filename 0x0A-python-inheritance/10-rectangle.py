#!/usr/bin/python3
""" 10-square - contains definition of class Rectangle """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class Rectangle inherits fom Rectangle """

    def __init__(self, size):
        """instantiation of the rectangle"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Return the area of rectangle """
        return self.__size ** 2
