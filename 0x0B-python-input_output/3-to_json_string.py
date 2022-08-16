#!/usr/bin/python3
""" 3-to_json_string.py - contains definition of to_json_string.py function """


import json


def to_json_string(my_obj):
    """ returns the JSON representation of an object (string) """
    return json.dumps(my_obj)
