#!/usr/bin/python3
"""

This module has one function returns a list with all values multiplied by a number

"""


def multiply_list_map(my_list=[], number=0):
    """
    Returns a list with all values multiplied by a number

    Args:
        my_list: The initial list
        number: The num each element of the lest will be multiplied by

    Return:
        new_list: The new list
    """

    return (list(map(lambda x: x*2, my_list)))
