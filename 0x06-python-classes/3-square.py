#!/usr/bin/python3
"""Make a class square."""


class Square:
    """Represent the square"""

    def __init__(self, size=0):
        """Initialize the new square.
        Args:
            size (int): Size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area"""
        return (self.__size ** 2)
