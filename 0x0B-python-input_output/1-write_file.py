#!/usr/bin/python3

def write_file(filename="", text=""):
    with open(filename, mode='w', encoding='UTF_8') as file:
        new = file.write(text)
        return new
