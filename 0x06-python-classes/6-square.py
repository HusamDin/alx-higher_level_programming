#!/usr/bin/python3
"""Define a square by: (based on 3-square.py)."""


class Square:
    """Define a square by: (based on 4-square.py)."""

    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
        if position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        if not (isinstance(position, tuple) or isinstance(position[0], int) not isinstance(position[1], int)):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = position

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
    
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        if not (isinstance(value, tuple) or isinstance(value[0], int) or isinstance(value[1], int)):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = position

    def area(self):
        return self.size ** 2

    def my_print(self):
        if self.size == 0:
            print()
        for i in range(self.size):
            print('_' * self.position[0] + '#' * self.size + '$' * self.position[1])
