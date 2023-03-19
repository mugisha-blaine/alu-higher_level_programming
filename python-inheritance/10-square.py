#!/usr/bin/python3
"""
rectangle class
"""


Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """ define square """
    def __init__(self, size):
        """ instantiation with size """
        self.__size = size
    def area(self):
        """ find an area """
        return self.__size * self.__size
