#!/usr/bin/python3

def append_write(filename="", text=""):
    with open(filename, mode='a', encoding='UTF-8') as file:
        new = file.write(text)
        return new