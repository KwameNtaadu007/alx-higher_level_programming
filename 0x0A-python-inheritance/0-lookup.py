#!/usr/bin/python3

def lookup(obj):
    attributes = []
    methods = []

    # Get the list of attributes and methods
    for item in dir(obj):
        if not item.startswith('__'):
            if callable(getattr(obj, item)):
                methods.append(item)
            else:
                attributes.append(item)

    # Return the combined list of attributes and methods
    return attributes + methods

