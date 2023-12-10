#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    new_list = []
    new_list = my_list.copy()
    del my_list[:]
    for i, element in enumerate(new_list):
        if i != idx:
            my_list.append(element)
    return my_list
