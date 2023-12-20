#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(0, list_length):
        res = 0
        try:
            if (type(my_list_1[i]) is int or type(my_list_1) is float) and \
                    (type(my_list_2[i]) is int or type(my_list_2) is float):
                res = my_list_1[i] / my_list_2[i]
            else:
                raise TypeError
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(res)
    return new_list
