#!/usr/bin/python3

def uppercase(str):
    output = ""
    for s in str:
        if ord(s) >= 97 and ord(s) <= 122:
            output += chr(ord(s) - 32)
        else:
            output += s
    print("{}".format(output))
