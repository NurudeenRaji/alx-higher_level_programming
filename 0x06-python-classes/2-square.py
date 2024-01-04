#!/usr/bin/python3
""" This is a  script to create a Square class """


class Square:
    """ The square class with a private instance attribute """

    def __init__(self, size=0):
        """ Constructor initialized with arguments.

        size : int
            A private size of the square
        """

        try:
            if type(size) is not int:
                raise TypeError
            elif size < 0:
                raise ValueError
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")

        self.__size = size
