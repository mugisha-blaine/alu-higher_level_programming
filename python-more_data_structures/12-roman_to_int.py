#!/usr/bin/python3
def roman_to_int(roman_string):
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    romans['IV'] = 4
    romans['IX'] = 9
    romans['XL'] = 40
    romans['XC'] = 90
    romans['CD'] = 400
    romans['CM'] = 900
    if not roman_string or not isinstance(roman_string, str):
        return 0
    n = 0
    i = 0
    while i < len(roman_string):
        if i+1 < len(roman_string) and roman_string[i:i+2] in romans:
            n += romans[roman_string[i:i+2]]
            i += 2
        else:
            n += romans[roman_string[i]]
            i += 1
    return n
