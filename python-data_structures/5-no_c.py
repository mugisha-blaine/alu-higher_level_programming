#!/usr/bin/python3
def no_c(my_string):
    new = ""
    for a in my_string:
        if (a is not 'c') or (a is not 'C'):
            new = new + a
    return new       
