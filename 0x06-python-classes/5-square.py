#!/usr/bin/python3
class Square:
    """Represents a square.

    This class defines a square with an optional size.

    Attributes:
        _size (int): The size of the square.

    Raises:
        TypeError: If the size is not an integer.
        ValueError: If the size is less than 0.

    Methods:
        area(): Calculate the area of the square.
    """

    def __init__(self, size=0):
        """Initialize the Square instance.

        Args:
            size (int, optional): The size of the square (default is 0).

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not size is not int: 
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._size = size

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self._size * self._size
    
    @property
    def size(self):
        """Getter method for the size attribute.

        Returns:
            int: The size of the square.
        """
        return self._size
    
    @size.setter
    def size(self, value):
        """Setter method for the size attribute.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, int):  
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value


    def my_print(self):
        """Public instance method that prints in stdout the square with the character #

        Prints:
            if size is equal to 0, print an empty line
            the square with the character #
        """
        if self._size <= 0:
            print()
        else:
            for i in range(self._size):
                for j in range(self._size):
                    print("#", end ="")
                print()
