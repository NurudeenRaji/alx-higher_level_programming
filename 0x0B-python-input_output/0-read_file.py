#!/usr/bin/python3

def read_file(filename=""):
    """ Function that reads a text file and prints it to stdout """
    with open(filename, encoding='utf-8') as file:
        a = file.read()
        print(a)
