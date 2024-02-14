#!/usr/bin/python3
""" module 5. Save Object to a file """
import json


def save_to_json_file(my_obj, filename):
    """ function that writes an Object to a text file, using a JSON """

    with open(filename, mode='w', encoding="UTF-8") as file:
        json.dump(my_obj, file)
