#!/usr/bin/python3
""" 2-is_same_class module """


def is_same_class(obj, a_class):
    """ A function to check the type of obj """

    if type(obj) is a_class:
        return True
    else:
        return False
