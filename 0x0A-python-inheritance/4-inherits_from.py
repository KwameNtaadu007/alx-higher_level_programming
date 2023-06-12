#!/usr/bin/python3

"""
 Check if an object is an instance of a class that 
    inherited (directly or indirectly)
    from the specified class.
"""

def inherits_from(obj, a_class):
    """
    Returns:
        True if the object is an instance of a class that inherited from the specified class,
        False otherwise.
    """
    # Get the object's class and check if it is a subclass of the specified class
    return issubclass(type(obj), a_class) and type(obj) != a_class

