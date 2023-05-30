#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Function prints x elements of a list.
    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements being printed.
    Returns:
        The number of elements printed.
    """
    try:
        elements = my_list[:x]
        print("".join(str(elem) for elem in elements))
        return len(elements)
    except IndexError:
        print("")
        return 0

