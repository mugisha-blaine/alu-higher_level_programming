#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new = my_list.copy()
    for x in my_list:
        if x % 2 == 0:
            new[x] = 1
        else:
            new[x] = 0
    return new
