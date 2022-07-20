#!/usr/bin/python3
def weight_average(my_list=[]):
    new_list, coef, note = [(x * y, y) for x, y in my_list], 0, 0
    for x, y in new_list:
        coef += y
        note += x
    try:
        return note / coef
    except ZeroDivisionError:
        return 0
