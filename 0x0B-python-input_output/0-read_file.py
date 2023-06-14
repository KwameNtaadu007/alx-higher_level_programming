#!/usr/bin/python3
"""A function that reads a file"""

def read_file(filename=""):
    """read and print its content to stdout """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")

