#!/usr/bin/python3
def no_c(my_string):
    for a in my_string:
        if a == 'c' or a == 'C':
            del 'c', 'C'
        return my_string
