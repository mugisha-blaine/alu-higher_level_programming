#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    items = argv[1:]
    count = len(items)
    operator = ['+', '-', '*', '/']
    if count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    elif argv[2] not in operator:
        print('Only +, -, * and / can be used')
    else:
        if argv[2] == operator[0]:
            a = int(items[0])
            b = int(items[2])
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif argv[2] == operator[1]:
            a = int(items[0])
            b = int(items[2])
            print('{} - {} = {}'.format(a, b, sub(a, b)))
        elif argv[2] == operator[2]:
            a = int(items[0])
            b = int(items[2])
            print('{} * {} = {}'.format(a, b, mul(a, b)))
        else:
            a = int(items[0])
            b = int(items[1])
            print('{} / {} = {}'.format(a, b, div(a, b)))
