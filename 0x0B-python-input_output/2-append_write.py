#!/usr/bin/python3
""" modele 2. Append to a file """


def append_write(filename="", text=""):
    """ function that appends a string at the end of a text
        and returns the number of characters """

    with open(filename, mode='a', encoding='UTF-8') as file:
        new = file.write(text)
        return new
