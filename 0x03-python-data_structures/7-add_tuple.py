#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    add_of_tuple = []
    for i in range(2):
        a = tuple_a[i] if len(tuple_a) >= (i + 1) else 0
        b = tuple_b[i] if len(tuple_b) >= (i + 1) else 0
        add_of_tuple.append(a + b)

    return tuple(add_of_tuple)
