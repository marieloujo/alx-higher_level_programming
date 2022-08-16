#!/usr/bin/python3
""" 2-append_write - contains append_write function """


def append_write(filename="", text=""):
    """ Appends text to the file
    Args:
        filename (string): name of file or it's path
        text (string): content of the file
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
