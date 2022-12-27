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

        if (not isinstance(position, tuple) or
               len(position) != 2 or not
               all(isinstance(num, int) for num in position) or not
               all(num >= 0 for num in position)):
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
        self.size = size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or not
                all(isinstance(num, int) for num in value) or not
                all(num >= 0 for num in value)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.position = value

    def area(self):
        return self.size ** 2

    def my_print(self):
        if self.size == 0:
            print()
            return

        [print() for i in range(self.position[1])]
        for i in range(self.size):
            [print(' ', end='') for j in range(self.position[0])]
            [print('#', end='') for k in range(self.size)]
            print()
