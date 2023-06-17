#!/usr/bin/python3
""" base """

class Base:
    """
    Base class for managing id attribute in derived classes.

    Attributes:
        __nb_objects (int): The number of instantiated objects.
        id (int): The identity of the object.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new Base object.

        Args:
            id (int, optional): The identity of the object. Defaults to None.
                If provided, assigns the id to the object. Otherwise, increments
                the __nb_objects attribute and assigns the new value to the id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

