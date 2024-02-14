#!/usr/bin/python3
""" module 8. Class to JSON """


def class_to_json(obj):
    """ function that returns the dictionary description
        with simple data structure
    """

    return obj.__dict__
