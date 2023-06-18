#!/usr/bin/python3


from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a Square, inheriting from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The size of the Square.
            x (int): The x-coordinate of the Square's position.
            y (int): The y-coordinate of the Square's position.
            id (int): The identity of the Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the Square.

        Returns:
            int: The size of the Square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the Square.

        Args:
            value (int): The size value to set.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string representation of the Square.

        Returns:
            str: The string representation of the Square.
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    def update(self, *args, **kwargs):
        """Update the attributes of the Square.

        Args:
            *args: List of arguments.
            **kwargs: Dictionary of keyword arguments.
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, attrs[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
    def to_dictionary(self):
        """Return the dictionary representation of the Square.

        Returns:
            dict: The dictionary representation of the Square.
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y,
        }
