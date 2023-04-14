#!/usr/bin/python3
"""
    contains Base Class for this project
"""
import json
import csv


class Base:
    """
        base class for this whole project
        Attributes:
            __nb_objs (int)
            id (int)
        Methods:
            __init__()
    """

    __nb_objs = 0

    def __init__(self, id=None):
        """
           Initializes the class attributes
           Args:
               id (int)
        """
        if id is None:
            Base.__nb_objs += 1
            self.id = Base.__nb_objs
        else:
            self.id = id
