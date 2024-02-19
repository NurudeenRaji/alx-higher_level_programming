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
        self.__width = val

    @property
    def height(self):
        """ getter for private class attributes - height """
        return self.__height

    @height.setter
    def height(self, val):
        """ setter for private class attributes  - height """
        self.__height = val

    @property
    def x(self):
        """ getter for private class attributes - x """
        return self.__x

    @x.setter
    def x(self, val):
        """ setter for private class attributes  - x """
        self.__x = val

    @property
    def y(self):
        """ getter for private class attributes - y """
        return self.__y

    @y.setter
    def y(self, val):
        """ setter for private class attributes  - y """
        self.__y = val

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor to initiate the class and inherited attributes """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
