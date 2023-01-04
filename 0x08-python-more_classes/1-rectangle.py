#!/usr/bin/python3
"""Class Rectangle that defines a rectangle by: (based on 0-rectangle.py"""


class Rectangle:
    """Rectangle based on 0-rectangle.py"""
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
