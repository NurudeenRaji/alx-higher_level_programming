#!/usr/bin/python3
""" This is a  script to create a Square class """


class Square:
    """ The square class with a private instance attribute """

    def __init__(self, size=0):
        """ Constructor initialized with arguments.

        size : int
            A private size of the square
        """
        self.__size = size

        try:
            if type(self.__size) is not int:
                raise TypeError
            elif self.__size < 0:
                raise ValueError
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")

    def area(self):
        """ A method that returns the area of the square """
        return (self.__size * self.__size)
