#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if length == 0:
        return None
    big = my_list[0]
    for x in my_list:
        if x > big:
            big = x
    return big
