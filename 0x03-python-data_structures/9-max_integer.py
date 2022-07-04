#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max = 0
    for elm in my_list:
        if elm > max:
            max = elm
    return max
