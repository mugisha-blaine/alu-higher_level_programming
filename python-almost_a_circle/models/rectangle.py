#!/usr/bin/python3
"""
    contains Rectangle class that implements Base class
"""
from models.base import Base


class Rectangle(Base):
    """
        class Rectangle implements Base class
        Methods:
            __init__()
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Initializes class instance
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
            getter function for __width
            Returns: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            setter function for width
            Args:
                value (int): value to be set
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """
            getter function for height
            Returns: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            setter function for height
            Args:
                value (int): value to be set
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """
            getter function for x
            Returns: x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
            setter function for x
            Args:
                value (int): value to be set
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """
            getter function for y
            Returns: y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
            setter function for y
            Args:
                value (int): value to be set
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        '''
            Returns the area of the rectangle
        '''
        return (self.height * self.width)

    def display(self):
        '''
            Prints to stdout the representation of the rectangle
        '''
        rectangle = ""
        print("\n" * self.y, end="")
        for x in range(self.height):
            rectangle += (" " * self.x) + ("#" * self.width) + "\n"
        print(rectangle, end="")

    def __str__(self):
        '''
            returns a string formart of the rectangle
        '''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        '''
            Updates the arguments in the class
        '''
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """return dictonary
        """
        return {'x': getattr(self, "x"), 'y': getattr(self, "y"),
                'id': getattr(self, "id"), 'height': getattr(self, "height"),
                'width': getattr(self, "width")}
