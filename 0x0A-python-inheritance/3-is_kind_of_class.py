#!/usr/bin/python3
""" 3-is_kind_of_class module """


def is_kind_of_class(obj, a_class):
    """ A function that checks for a instance of a object """

    if isinstance(obj, a_class):
        return True
    else:
        return False
