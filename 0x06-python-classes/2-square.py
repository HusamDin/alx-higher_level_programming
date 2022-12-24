#!/usr/bin/python3
"""
Defines a square with private instance attribute: size.
Instantiation with optional size with conditions if provided.
"""


class Square:
    """Represents a square with Private instance attribute: size."""
    def __init__(self, size=0):
        # if type(size) == int:
        if isinstance(size, int):
            self.__size = size
        else:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')
