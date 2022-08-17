#!/usr/bin/python3
""" Module - 8-class_to_json.py """


import json


def class_to_json(obj):
    """ Class object to json """
    return obj.__dict__
