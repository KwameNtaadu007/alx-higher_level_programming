#!/usr/bin/python3

"""
Module to find the max integer in a list
"""

def max_integer(lst=[]):
    """
    Finds and returns the maximum integer in a list of integers.

    Args:
        lst (list): The list of integers.

    Returns:
        int or None: The maximum integer in the list. If the list is empty, returns None.
    """
    if len(lst) == 0:
        return None

    result = lst[0]
    for num in lst:
        if num > result:
            result = num

    return result

