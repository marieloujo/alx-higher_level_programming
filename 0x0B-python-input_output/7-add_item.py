#!/usr/bin/python3
""" 7-add_item.py -
    adds all arguments to a Python list,
    and then save them to a file
"""


import json, sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


if __name__ == "__main__":
    filename = 'add_item.json'
    my_list = []
    with open(filename, 'w', encoding="utf-8") as f:
        try:
            my_list = load_from_json_file(filename)
        except json.JSONDecodeError:
            pass
        my_list.extend(sys.argv[1:])
        save_to_json_file(my_list, filename)
