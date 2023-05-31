class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
            position (tuple): The position of the new square.
        """
        self._size = self._validate_size(size)
        self._position = self._validate_position(position)

    def _validate_size(self, size):
        """Validate and return the size of the square."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        return size

    def _validate_position(self, position):
        """Validate and return the position of the square."""
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(num, int) for num in position) or not all(num >= 0 for num in position):
            raise ValueError("position must be a tuple of 2 positive integers")
        return position

    @property
    def size(self):
        """Get or set the size of the square."""
        return self._size

    @size.setter
    def size(self, value):
        self._size = self._validate_size(value)

    @property
    def position(self):
        """Get or set the position of the square."""
        return self._position

    @position.setter
    def position(self, value):
        self._position = self._validate_position(value)

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self._size ** 2

    def my_print(self):
        """Print the square with the '#' character."""
        if self._size == 0:
            print()
            return

        for _ in range(self._position[1]):
            print()
        for _ in range(self._size):
            print(" " * self._position[0] + "#" * self._size)

