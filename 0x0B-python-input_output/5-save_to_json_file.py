#!/usr/bin/python3
""" 5-save_to_json_file.py -
    contains definition of save_to_json_file.py function
"""


import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file, using a JSON representation
    Args:
        filename (string): name of file or it's path
        my_obj (object|any): object
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
