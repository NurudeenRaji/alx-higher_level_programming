#!/usr/bin/python3
""" 7-base_geometry.py """


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
        if type(self.value) is not int:
            raise TypeError("{} must be an integer".format(self.name))
        if self.value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
