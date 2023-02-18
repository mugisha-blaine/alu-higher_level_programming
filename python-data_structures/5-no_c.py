#!/usr/bin/python3
def no_c(my_string):
    str1 = my_string.lower('C')
    new = ""
    for a in str1:
        if (a != "c"):
            new = new + a
    return new
