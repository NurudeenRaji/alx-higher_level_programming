#!/usr/bin/python3
""" module 1. Base class """


class Base:
    """ This is the “base” of all other classes in this project.
        The goal of it is to manage id attribute in all our
        future classes and to avoid duplicating the same code
        (by extension, same bugs for the models packages) """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor to initiate the class and value of id """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
