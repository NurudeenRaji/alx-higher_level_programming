#!/usr/bin/python3
""" This is a  script to create a Square class """


class Square:
    """ The square class with a private instance attribute """

    def __init__(self, size):
        """ Constructor initialized with arguments.

        size : int
            The size of the square
        """
        self.__size = size
