#!/usr/bin/python3
def no_c(my_string):
    new_string = [letter for letter in my_string if letter not in ['c', 'C']]
    return "".join(new_string)
