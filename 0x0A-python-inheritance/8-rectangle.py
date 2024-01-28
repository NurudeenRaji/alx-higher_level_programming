#!/usr/bin/python3
""" 8-base_geometry module """

BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""BaseGeometry class module"""


class Rectangle(BaseGeometry):
    """ BaseGeometry class """

    def __init__(self, width, height):
        """ Constructor """

        self.__width = width
        self.__height = height

        self.integer_validator("width", width)
        self.integer_validator("height", height)
