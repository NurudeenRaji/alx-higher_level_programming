#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        temp = ["{:d}".format(i) for i in row]
        print(" ".join(temp))
