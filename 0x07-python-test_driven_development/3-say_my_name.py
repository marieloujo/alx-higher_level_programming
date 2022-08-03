#!/usr/bin/python3
"""
This is the "3-say_my_name" module.
The 3-say_my_name module supplies one function,
say_my_name(first_name, last_name="").
"""


def say_my_name(first_name, last_name=""):
    """
    Prints My name is <first name> <last name>

    Args:
        first_name (string): First name
        last_name (string): Last name,
        is optional and defauult value empty string

    Returns:
        Nothing
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
