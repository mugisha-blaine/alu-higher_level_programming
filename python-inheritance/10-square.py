#!/usr/bin/python3
"""
square class
"""


Rectangle = __import__('9-rectangle.py').Rectangle


''' Square class '''

class Square(Rectangle):
    """ define square """
    def __init__(self, size):
        """ instantiation with size """
        self.__size = size
    def area(self):
        """ find an area """
        return self.__size * self.__size
