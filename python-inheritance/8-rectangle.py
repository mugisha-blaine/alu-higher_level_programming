#!/usr/bin/python3
'''Inherit from other class.'''


class Rectangle(BaseGeometry):
    '''Implements a rectangle.'''

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
