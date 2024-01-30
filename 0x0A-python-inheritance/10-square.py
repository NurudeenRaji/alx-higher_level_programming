#!/usr/bin/python3
""" 10-square module """
Rectangle = __import__("9-rectangle").Rectangle
""" Rectangl class module imported """


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
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
