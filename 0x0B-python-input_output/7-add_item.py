#!/usr/bin/python3
""" 7-add_item.py -
    adds all arguments to a Python list,
    and then save them to a file
"""


import json
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


filename = 'add_item.json'
my_list = []

try:
    my_list = load_from_json_file(filename)
except json.JSONDecodeError:
    pass
my_list.extend(sys.argv[1:])
save_to_json_file(my_list, filename)
