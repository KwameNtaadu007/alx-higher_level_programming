class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes the square.

        Args:
            size (int): Size of a side of the square.
        """
        self._size = self._validate_size(size)

    def _validate_size(self, size):
        """Validates and returns the size of the square."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        return size

    @property
    def size(self):
        """Getter for the size of the square."""
        return self._size

    @size.setter
    def size(self, value):
        """Setter for the size of the square."""
        self._size = self._validate_size(value)

    def area(self):
        """Calculates the area of the square.

        Returns:
            The area of the square.
        """
        return self._size ** 2

    def my_print(self):
        """Prints the square."""
        if self._size == 0:
            print()
            return
        for _ in range(self._size):
            print("#" * self._size)

