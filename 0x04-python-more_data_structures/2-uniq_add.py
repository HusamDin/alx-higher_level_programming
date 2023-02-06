#!/usr/bin/python3
"""

This module has one function to add all unique integers in a list

"""


def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list

    Args:
        my_list: The target list

    Return:
        The result of the addition of all unique elements in my_list
    """
    result = 0
    uniq_list = set(my_list)

    for i in uniq_list:
        result += i

    return (result)
