#!/usr/bin/python3

def read_file(filename=""):
    """ Function that reads a text file and prints it to stdout """
    with open(filename, encoding='UTF-8') as file:
        a = file.read()
        print(a)
