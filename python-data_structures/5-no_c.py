#!/usr/bin/python3
def no_c(my_string):
    new = ""
    for a in my_string:
        if (a != 'c') or (a != 'C'):
            new = new + a
    return new       