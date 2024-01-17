#!/usr/bin/python3

"""
Addition of two integers

This module has only one function.
"""


def add_integer(a, b=98):
    """
    A function adding two integers

    param a: the first integer
    param b: has default value of 98.
    return: the sum of the two parameter.
    """

    if not (type(a) is int or type(a) is float):
        raise TypeError("a must be an integer")
    if not (type(b) is int or type(b) is float):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
