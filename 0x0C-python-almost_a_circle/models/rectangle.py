#!/usr/bin/python3
""" Module - rectangle
from models.base import Base
Base = __import__('base').Base
"""


from models.base import Base


class Rectangle(Base):
    """ Definition of Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Create new rectangle """
        super().__init__(id)
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    @property
    def height(self):
        """Retrieve of private attribute __height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the value of __height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def width(self):
        """Retrieve of private attribute __width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the value of __width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def x(self):
        """Retrieve of private attribute __x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the value of __x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrieve of private attribute __y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the value of __y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Compute the area of rectangle

        Returns:
            Int: value of area
        """
        return self.height * self.width

    def __str__(self):
        """ String representation of rectangle """
        return "[Rectangle] (" +\
               "{s.id}) {s.x}/{s.y} - {s.width}/{s.height}".format(s=self)

    def display(self):
        """ Prints rectangle with '#' charater """
        print("\n" * self.y, end='')
        print("\n".join((" " * self.x) + ("#" * self.width)
              for j in range(self.height)))

    def update(self, *args, **kwargs):
        """ Update the class Rectangle """
        if (args):
            arguments = {0: 'id', 1: 'width', 2: 'height', 3: 'x', 4: 'y'}
            for i in range(len(args)):
                setattr(self, arguments[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of a Rectangle """
        return self.__dict__
