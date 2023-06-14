#!/usr/bin/python3


def is_same_class(obj, a_class):
    """
    Check if an object is an instance of a specific class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of the specified class, False otherwise.
    """
    # Compare the type of the object with the specified class
    if type(obj) == a_class:
        return True
    else:
        return False

