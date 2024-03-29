#!/usr/bin/python3
"""
Function that prints a square
"""


def print_square(size):
    """
    Prints a square with #
    size(param): the size of the square we want to print.
    Return: nothing
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(0, size):
        for j in range(0, size):
            print("#", end="")
        print("\n", end="")
