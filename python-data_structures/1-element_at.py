#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return none
    elif idx > len(my_list):
        return none
    for x in my_list:
        print("Element at index {:d} is {}".format(idx, x)) 
