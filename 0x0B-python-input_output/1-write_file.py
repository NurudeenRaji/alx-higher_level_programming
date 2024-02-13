#!/usr/bin/python3
""" module 1. Write to a file """


def write_file(filename="", text=""):
    """ function that writes a string to a text file
        and returns the number of characters """

    with open(filename, mode='w', encoding='UTF_8') as file:
        new = file.write(text)
        return new
