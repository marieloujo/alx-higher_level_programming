#!/usr/bin/python3
"""
This is the "4-print_square" module.
The 4-print_square module supplies one function,
print_square(size):.
"""


def print_square(size):
    """
    prints a square with the character #

    Args:
        size (int): size length of square
    Returns: nothing
    """
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print(("#" * size + "\n") * size, end="")
