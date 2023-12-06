#!/usr/bin/python3

def print_last_digit(number):
    last_num = abs(number) % 10
    if last_num < 0:
        last_num = -lastnum
    print(last_num, end= '')
    return last_num
