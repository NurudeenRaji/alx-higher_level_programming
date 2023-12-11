#!/usr/bin/python3

def uniq_add(my_list=[]):
    new = set(my_list)
    sums = 0
    for i in new:
        sums += i
    return sums
