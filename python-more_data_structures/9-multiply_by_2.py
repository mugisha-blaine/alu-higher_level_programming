#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    multi = a_dictionary.copy()
    for a in multi.keys():
        multi[a] = multi * 2
    return multi
