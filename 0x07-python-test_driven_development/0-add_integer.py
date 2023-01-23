#!/usr/bin/python3
"""

    This module has one function to add up two integers

"""


def add_integer(a, b=98):
    """Return the sum of two integers or floats as integers

    Args:
        a: first argument
        b: second argument

    Returns:
        Sum of the two arguments

    Raises:
        TypeError: if either of the two arguments not an integer or a float
    """
    if isinstance(a, int) or isinstance(a, float):
        if isinstance(b, int) or isinstance(b, float):
            return (int(a) + int(b))
        else:
            raise TypeError('b must be an integer')
    else:
        raise TypeError('a must be an integer')
