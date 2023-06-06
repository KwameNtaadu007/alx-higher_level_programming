#!/usr/bin/python3
"""
Defines a class Rectangle
"""


class Rectangle:
    """Representation of a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """prints a string when an instance has been deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def _validate_dimension(value):
        """Validates a dimension value"""
        if type(value) is not int:
            raise TypeError("Dimension must be an integer")
        if value < 0:
            raise ValueError("Dimension must be >= 0")

    @property
    def width(self):
        """getter for the private instance attribute width"""
        return self._width

    @width.setter
    def width(self, value):
        """setter for the private instance attribute width"""
        self._validate_dimension(value)
        self._width = value

    @property
    def height(self):
        """getter for the private instance attribute height"""
        return self._height

    @height.setter
    def height(self, value):
        """setter for the private instance attribute height"""
        self._validate_dimension(value)
        self._height = value

    def area(self):
        """returns the area of the rectangle"""
        return self._width * self._height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self._width == 0 or self._height == 0:
            return 0
        return (self._width * 2) + (self._height * 2)

    def __str__(self):
        """returns printable string representation of the rectangle"""
        if self._width == 0 or self._height == 0:
            return ""
        return "\n".join(str(self.print_symbol) * self._width
                for _ in range(self._height))

        def __repr__(self):
            """returns a string representation of the rectangle for reproduction"""
        return f"Rectangle({self._width}, {self._height})"

