#!/usr/bin/python3
""" base """

import json

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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: The JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances.

        Returns:
            None
        """
        filename = cls.__name__ + ".json"
        json_string = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        with open(filename, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by the JSON string.

        Args:
            json_string (str): A string representing a list of dictionaries.

        Returns:
            list: The list represented by the JSON string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with all attributes already set using a dictionary.

        Args:
            **dictionary: Keyword arguments representing the attributes of the instance.

        Returns:
            Base: An instance of the class with the attributes set according to the dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)  # Create a dummy instance of Rectangle
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)  # Create a dummy instance of Square

        dummy_instance.update(**dictionary)  # Update the dummy instance with the actual attribute values

        return dummy_instance
