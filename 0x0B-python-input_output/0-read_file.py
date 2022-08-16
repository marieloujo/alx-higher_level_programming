#!/usr/bin/python3
""" 0-read_file - contain function read_file """


def read_file(filename=""):
    """ Open file in reading mode and prints it content to stdout
    Args:
        filename(string): name of file or it's path
    """
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end='')
