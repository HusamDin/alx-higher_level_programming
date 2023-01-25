#!/usr/bin/python3
"""

    This module has one function to print a square

"""


def print_square(size):
    """

    This function prints a square of size size

    Args:
        size: an int

    Raises:
        TypeError: if size is not an int
        ValueError: if size is less than 0

    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        print('#' * size)
