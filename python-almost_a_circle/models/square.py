#!/usr/bin/python3
"""Define Rectangle Class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Representation of Square
"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization of a Square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Square size getter
        """
        return self.width

    @size.setter
    def size(self, value):
        """Square size setter
        """
        self.width = value
        self.height = value

    def __str__(self):
        """ string represation of square
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)
