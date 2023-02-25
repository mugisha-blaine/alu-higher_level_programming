#!/usr/bin/python3
def roman_to_int(roman_string):
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    romans['IV'] = 4
    romans['IX'] = 9
    romans['XL'] = 40
    romans['XC'] = 90
    romans['CD'] = 400
    romans['CM'] = 900
    if roman_string and type(roman_string) == str:
        n = 0
        for i in range(len(roman_string)):
            for j in romans.keys():
                if roman_string[:] is j:
                    n = romans[j]
                    return n
                if roman_string[i:] is j:
                    n += romans[j]
                    break
        return n
    else:
        return 0
