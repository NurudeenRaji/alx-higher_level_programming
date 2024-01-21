#!/usr/bin/python3

"""
A function to print my name.
"""


def say_my_name(first_name, last_name=""):
    """
    Function to print first_name & last_name

    first_name: first param
    last_name: Second param
    return: nothing.
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
