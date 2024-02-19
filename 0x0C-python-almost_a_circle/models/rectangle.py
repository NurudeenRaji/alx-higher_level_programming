#!/usr/bin/python3
""" module 2. First Rectangle """
from models.base import Base
"""Base class imported from models.base module """


class Rectangle(Base):
    """ A rectangle class that inherits from the base class as its
        superclass """

    @property
    def width(self):
        """ getter for private class attributes - width """
        return self.__width

    @width.setter
    def width(self, val):
        """ setter for private class attributes  - width """
        if not isinstance(val, int):
            raise TypeError("width must be a integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @property
    def height(self):
        """ getter for private class attributes - height """
        return self.__height

    @height.setter
    def height(self, val):
        """ setter for private class attributes  - height """
        if not isinstance(val, int):
            raise TypeError("height must be a integer")
        if val <= 0:
            raise ValueError("height must be > 0")
        self.__height = val

    @property
    def x(self):
        """ getter for private class attributes - x """
        return self.__x

    @x.setter
    def x(self, val):
        """ setter for private class attributes  - x """
        if not isinstance(val, int):
            raise TypeError("x must be a integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        """ getter for private class attributes - y """
        return self.__y

    @y.setter
    def y(self, val):
        """ setter for private class attributes  - y """
        if not isinstance(val, int):
            raise TypeError("y must be a integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor to initiate the class and inherited attributes """
        if not isinstance(width, int):
            raise TypeError("width must be a integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if not isinstance(height, int):
            raise TypeError("height must be a integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if not isinstance(x, int):
            raise TypeError("x must be a integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if not isinstance(y, int):
            raise TypeError("y must be a integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
