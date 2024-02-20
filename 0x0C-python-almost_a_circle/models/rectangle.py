#!/usr/bin/python3
""" module 2. First Rectangle """
from models.base import Base
"""Base class imported from models.base module """


class Rectangle(Base):
    """ A rectangle class that inherits from the base class as its
        superclass """

    @property
    def width(self):
        """ getter for private class attributes - width """
        return self.__width

    @width.setter
    def width(self, val):
        """ setter for private class attributes  - width """
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @property
    def height(self):
        """ getter for private class attributes - height """
        return self.__height

    @height.setter
    def height(self, val):
        """ setter for private class attributes  - height """
        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        if val <= 0:
            raise ValueError("height must be > 0")
        self.__height = val

    @property
    def x(self):
        """ getter for private class attributes - x """
        return self.__x

    @x.setter
    def x(self, val):
        """ setter for private class attributes  - x """
        if not isinstance(val, int):
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        """ getter for private class attributes - y """
        return self.__y

    @y.setter
    def y(self, val):
        """ setter for private class attributes  - y """
        if not isinstance(val, int):
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor to initiate the class and inherited attributes """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def area(self):
        """ Public method that returns the area of the rectangle """
        return self.__width * self.__height

    def display(self):
        """ Public method that prints in stdout the Rectangle instance
            with the character - # """

        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            for _ in range(self.__x):
                print(" ", end="")
            for _ in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """ Public method to override the __str__ method """

        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """ public method that assigns an argument to each attribute """

        attributes = ['id', '_Rectangle__width', '_Rectangle__height',
                      '_Rectangle__x', '_Rectangle__y']
        if args:
            for attribute, value in zip(attributes, args):
                setattr(self, attribute, value)

        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
