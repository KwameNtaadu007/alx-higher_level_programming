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

    def area(self):
        """Returns the area of the rectangle"""
        return self._width * self._height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self._width == 0 or self._height == 0:
            return 0
        return (self._width * 2) + (self._height * 2)

    def __str__(self):
        """Returns a string representation of the rectangle"""
        if self._width == 0 or self._height == 0:
            return ""
        return "\n".join("#" * self._width for _ in range(self._height))

