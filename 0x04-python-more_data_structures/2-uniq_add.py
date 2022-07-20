#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for elm in set(my_list):
        sum += elm
    return sum
