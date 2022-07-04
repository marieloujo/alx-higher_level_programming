#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    for item in zip(tuple_a, tuple_b):
        print(item)

tuple_a = (1, 89)
tuple_b = (88, 11)
""" add_tuple(tuple_a, tuple_b) """
add_tuple(tuple_a, (1, ))
""" add_tuple(tuple_a, ()) """