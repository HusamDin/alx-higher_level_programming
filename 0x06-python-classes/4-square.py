#!/usr/bin/python3
"""Define a square by: (based on 3-square.py)."""


class Square:
    """Define a square by: (based on 3-square.py)."""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        return self.size ** 2
