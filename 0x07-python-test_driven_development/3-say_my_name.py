#!/usr/bin/python3

"""
This module contains a function that prints a message with a given name.
"""


def say_my_name(first_name, last_name=""):
    """Prints a message "My name is <first name> <last name>".

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to "".

    Returns:
        None.

    Raises:
        TypeError: If either the first name or last name is not a string.

    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))

