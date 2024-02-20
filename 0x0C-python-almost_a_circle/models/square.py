#!/usr/bin/python3
""" Module conatining the Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square cass that inherits from the class Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor for the square class """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                self.y, self.height))
