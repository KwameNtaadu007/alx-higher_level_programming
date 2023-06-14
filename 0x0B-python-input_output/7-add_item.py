#!/usr/bin/python3
"""
Script that adds all arguments to a Python list, and then saves them to a file
"""

from sys import argv
from json import dumps
from os.path import exists, isfile


def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as file:
        file.write(dumps(my_obj))


def load_from_json_file(filename):
    with open(filename, 'r') as file:
        return loads(file.read())


filename = "add_item.json"

if not exists(filename) or not isfile(filename):
    json_list = []
else:
    json_list = load_from_json_file(filename)

for arg in argv[1:]:
    json_list.append(arg)

save_to_json_file(json_list, filename)

