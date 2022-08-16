#!/usr/bin/python3
""" Module that defines a MyList class
"""


class MyList(list):
    """ Define class MyList herite from class list """

    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """
            Prints the list in ascending sorted order
        """
        print(sorted(self))
