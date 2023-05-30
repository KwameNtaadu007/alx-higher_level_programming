#!/usr/bin/python3

def safe_print_integer(value):
    """Function prints an integer with "{:d}".format().
    Args:
        value (int): The integer being printed.
    Returns:
        True if the integer is successfully printed, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False

