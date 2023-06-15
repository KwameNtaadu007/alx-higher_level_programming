#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""

def add_attribute(obj, attr, value):
    """Adds a new attribute to an object if possible."""
    if hasattr(obj, "__dict__"):
        obj.__dict__[attr] = value
    else:
        raise TypeError("can't add new attribute")

