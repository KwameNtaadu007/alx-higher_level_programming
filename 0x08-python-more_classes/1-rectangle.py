#!/usr/bin/python3

"""
Defines a class Rectangle
"""

class Rectangle:
    """Representation of a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""
        self._width = self._validate_dimension(width)
        self._height = self._validate_dimension(height)

    @property
    def width(self):
        """Getter for the width attribute"""
        return self._width

    @width.setter
    def width(self, value):
        """Setter for the width attribute"""
        self._width = self._validate_dimension(value)

    @property
    def height(self):
        """Getter for the height attribute"""
        return self._height

    @height.setter
    def height(self, value):
        """Setter for the height attribute"""
        self._height = self._validate_dimension(value)

    def _validate_dimension(self, value):
        """Helper method to validate the dimension value"""
        if not isinstance(value, int):
            raise TypeError("Dimension must be an integer")
        if value < 0:
            raise ValueError("Dimension must be >= 0")
        return value

