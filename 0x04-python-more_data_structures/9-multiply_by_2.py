#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new = {i: v * 2 for i, v in a_dictionary.items()}
    return new
