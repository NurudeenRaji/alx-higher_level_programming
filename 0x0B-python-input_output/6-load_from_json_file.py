#!/usr/bin/python3
""" module 6. Create object from a JSON file """
import json


def load_from_json_file(filename):
    """ function that creates an Object from a JSON file """

    with open(filename, encoding="UTF-8") as file:
        json.loads(filename)
