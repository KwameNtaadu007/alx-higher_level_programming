#!/usr/bin/python3
"""
Defines a class Rectangle
"""


class Rectangle:
    """Representation of a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance that is a square with width and height equal to size"""
        return cls(size, size)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""
        self._width = self._validate_dimension(width)
        self._height = self._validate_dimension(height)
        Rectangle.number_of_instances += 1

    def __del__(self):
        """prints a string when an instance has been deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """getter for the private instance attribute width"""
        return self._width

    @width.setter
    def width(self, value):
        """setter for the private instance attribute width"""
        self._width = self._validate_dimension(value)

    @property
    def height(self):
        """getter for the private instance attribute height"""
        return self._height

    @height.setter
    def height(self, value):
        """setter for the private instance attribute height"""
        self._height = self._validate_dimension(value)

    def area(self):
        """returns the area of the rectangle"""
        return self._width * self._height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self._width == 0 or self._height == 0:
            return 0
        return (self._width * 2) + (self._height * 2)

    def __str__(self):
        """returns a printable string representation of the rectangle"""
        if self._width == 0 or self._height == 0:
            return ""
        return "\n".join(str(self.print_symbol) * self._width for _ in range(self._height))

    def __repr__(self):
        """returns a string representation of the rectangle for reproduction"""
        return f"Rectangle({self._width}, {self._height})"

    @staticmethod
    def _validate_dimension(value):
        """validates and returns a non-negative integer value"""
        if not isinstance(value, int):
            raise TypeError("Dimension must be an integer")
        if value < 0:
            raise ValueError("Dimension must be >= 0")
        return value

