#!/usr/bin/python4
""" This is a  script to create a Square class """


class Square:
    """ The square class with a private instance attribute """

    def __init__(self, size=0):
        """ Constructor initialized with arguments.

        size : int
            A private size of the square
        """
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        try:
            if type(value) is not int:
                raise TypeError
            elif value < 0:
                raise ValueError
            self.__size = value
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")

    def area(self):
        """ A method that returns the area of the square """
        return (self.__size * self.__size)
