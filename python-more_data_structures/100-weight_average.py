#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == [] or my_list is None:
        return (0)
    mug = 0
    ni = 0
    for x, y in my_list:
        mug += x * y
        ni += y
    return (mug / ni)
