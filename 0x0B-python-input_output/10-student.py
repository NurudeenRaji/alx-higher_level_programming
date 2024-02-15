#!/usr/bin/python3
""" module 10. Student to JSON with filter """


class Student:
    """ Student class that defines a student """

    def __init__(self, first_name, last_name, age):
        """ Constructor method """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation of a Student instance """
        if attrs is None:
            return self.__dict__
        else:
            res = {}
            for attr in attrs:
                if hasattr(self, attr):
                    res[attr] = getattr(self, attr)
            return res
