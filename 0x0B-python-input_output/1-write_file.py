#!/usr/bin/python3
""" 1-write_file - contains write_file function """


def write_file(filename="", text=""):
    """ Open file in writing mode and put text into it
    Args:
        filename (string): name of file or it's path
        text (string): content of the file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
