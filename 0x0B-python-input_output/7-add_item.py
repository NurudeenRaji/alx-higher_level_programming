#!/usr/bin/python3
""" module 7. Load, add, save """
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
try:
    file = load_from_json_file(filename)
except FileNotFoundError:
    file = []

for i in range(1, len(sys.argv)):
    file.append(sys.argv[i])

save_to_json_file(file, filename)
