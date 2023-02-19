#!/usr/bin/python3
def max_integer(my_list=[]):
    big = my_list[0]
    length = len(my_list)
    if length == 0:
        return None
    for x in my_list:
        if x > big:
            big = x
    return big
