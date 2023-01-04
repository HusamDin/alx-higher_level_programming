#!/usr/bin/python3
"""Class Rectangle that defines a rectangle by: (based on 3-rectangle.py"""


class Rectangle:
    """Class Rectangle that defines a rectangle by: (based on 3-rectangle.py"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if isinstance(width, int):
            if width < 0:
                raise ValueError('width must be >= 0')
            self.__width = width
        else:
            raise TypeError('width must be an integer')

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if isinstance(height, int):
            if height < 0:
                raise ValueError('height must be >= 0')
            self.__height = height
        else:
            raise TypeError('height must be an integer')

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return self.width * 2 + self.height * 2

    def __str__(self):
        if not self.width or not self.height:
            return ""

        rec = ''

        for i in range(self.height):
            for j in range(self.width):
                rec += '#'
            if i != self.height - 1:
                rec += '\n'

        return (str(rec))
