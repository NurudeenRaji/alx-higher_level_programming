#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    size = len(my_list) - 1
    new_list = my_list.copy()
    if idx < 0:
        return my_list
    elif idx > size:
        return my_list
    else:
        new_list[idx] = element
        return new_list
