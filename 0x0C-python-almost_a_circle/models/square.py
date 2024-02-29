#!/usr/bin/python3
""" Module conatining the Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square cass that inherits from the class Rectangle """

    @property
    def size(self):
        """ getter method for the square size """
        return self.width

    @size.setter
    def size(self, val):
        """ setter method for the square size """
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.width = val
        self.height = val

    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor for the square class """
        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                self.y, self.height))

    def update(self, *args, **kwargs):
        """ Update function used to assign arguments to teh attributes """

        attributes = ['id', 'size', 'x', 'y']
        if args:
            setattr(self, attribute, value)
        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of a Sqaure class """

        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
