#!/usr/bin/python3

"""
Addition of two integers

This module has only one function.
"""


def add_integer(a, b=98):
    """
    A function adding two integers
    """

    if not (type(a) is int or type(a) is float):
        raise TypeError("a must be an integer")
    if not (type(b) is int or type(b) is float):
        raise TypeError("b must be an integer")

    res = a + b

    res = int(a) + int(b)

    return res
