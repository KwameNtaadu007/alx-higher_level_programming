#!/usr/bin/python3
"""
Contains the class MyInt
"""

class MyInt(int):
    """Represents a rebel integer."""

    def __eq__(self, other):
        """Override the equality operator (==)."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the inequality operator (!=)."""
        return super().__eq__(other)

