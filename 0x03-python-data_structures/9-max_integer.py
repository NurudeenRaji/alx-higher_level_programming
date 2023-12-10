#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        max_num = None
        for i in my_list:
            if max_num is None or i > max_num:
                max_num = i
        return max_num
