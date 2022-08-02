#!/usr/bin/python3
"""
This is the "0-add_integer" module.
The 0-add_integer module supplies one function, add_integer(a, b).
"""
import math


def add_integer(a, b=98):
    """
    Add two numbers :  integers or floats

    Args:
        a (int): first number
        b (int): second number, default value 98

    Returns:
        a + b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    a = int(a) if type(a) is float else a
    b = int(b) if type(b) is float else b
    return a + b
