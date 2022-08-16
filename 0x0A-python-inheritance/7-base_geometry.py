#!/usr/bin/python3
""" 5-base_geometry - contains BaseGeometry class definition
"""


class BaseGeometry:
    """ claas BaseGeometry """

    def area(self):
        """ method area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0")
