#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = [key for key, data in a_dictionary.items() if data is value]
    for key in keys:
        del a_dictionary[key]
    return a_dictionary
