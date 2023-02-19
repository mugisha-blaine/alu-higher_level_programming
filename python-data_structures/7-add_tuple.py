#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tot_a = len(tuple_a)
    tot_b = len(tuple_b)
    if tot_a == 0:
        tuple_a = (0, 0)
    elif tot_a == 1:
        tuple_a = (tuple_a[0], 0)
    if tot_b < 1:
        tuple_b = (0, 0)
    elif tot_b < 2:
        tuple_b = (tuple_b[0], 0)
    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return result
