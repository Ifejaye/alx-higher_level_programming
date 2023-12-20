#!/usr/bin/python3
class Square:
    """Represents a square.

    This class defines a square with an optional size.

    Attributes:
        _size (int): The size of the square.

    Raises:
        TypeError: If the size is not an integer.
        ValueError: If the size is less than 0.
    """
    def __init__(self, size=0):
        """Initialize the Square instance.

        Args:
            size (int, optional): The size of the square (default is 0).

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._size = size
