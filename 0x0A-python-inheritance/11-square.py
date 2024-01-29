#!/usr/bin/python3
"""10-square.py"""
Rectangle = __import__('10-square').Rectangle
"""Rectangle class module"""


class Square(Rectangle):
    """ Square class """

    def __init__(self, size):
        """ Constructor """
        self.__size = size

        self.integer_validator("size", size)

    def area(self):
        """ Area of the rectangle """
        return self.__size * self.__size

    def __str__(self):
        """Return a string representation of the square."""
        return ("[Square] {}/{}".format(self.__size, self.__size))
