#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        s = ""
        for i in row:
            s += str(i)
            s += " "
        s = s.rstrip()
        print("{}".format(s))
