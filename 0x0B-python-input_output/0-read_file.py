#!/usr/bin/python3

""" 0. Read file """


def read_file(filename=""):
    """ Function that reads a text file and prints it to stdout """

    with open(filename, encoding='UTF-8') as file:
        for a in file:
            print("{}".format(a), end="")
