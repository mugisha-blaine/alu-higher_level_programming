#!/usr/bin/python3
""" define a fuction that reads text files """


def read_file(filename=""):
    """a fuction to read text """
    with open(filename, 'r', encoding='UTF8') as b:
        print(b.read(), end='')
