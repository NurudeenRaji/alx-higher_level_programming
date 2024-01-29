#!/usr/bin/python3
""" 9-rectangle module """


class BaseGeometry:
    """ BaseGeometry class """

    def area(self):
        """An empty method """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        self.value = value

        if type(self.name) is not str:
            raise TypeError("name must be a string")
        if self.name is None or self.name is bool:
            raise TypeError("name must be a string")
        if len(self.name) == 0:
            raise TypeError("name must not be an empty string")

        if type(self.value) is not int:
            raise TypeError("{} must be an integer".format(self.name))
        if self.value is None or self.value is bool:
            raise TypeError("{} must be an integer".format(self.name))
        if self.value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))

class Rectangle(BaseGeometry):
    """ BaseGeometry class """

    def __init__(self, width, height):
        """ Constructor """

        self.__width = width
        self.__height = height

        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """ Calculates the area of the rectangle """
        return self.__width * self.__height
    def __str__(self):
        """ String representation of the retangle """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
