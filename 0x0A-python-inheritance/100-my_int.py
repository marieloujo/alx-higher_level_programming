#!/usr/bin/python3
""" Contains definition of class MyInt """


class MyInt(int):
    """ A class MyInt that inherits from int """

    def __eq__(self, c_int):
        """Compare if MyInt is equal another int
        Args:
            c_int (int): int to compare against
        Returns:
            True or False
        """
        return int(self) != c_int

    def __ne__(self, c_int):
        """Compare if MyInt is not equal to another int
        Args:
            c_int (int): int to compare against
        Returns:
            True or False
        """
        return int(self) == c_int
