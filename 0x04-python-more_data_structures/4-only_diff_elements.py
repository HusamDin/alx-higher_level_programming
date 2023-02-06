#!/usr/bin/python3
"""

This module has one function to return all elements in one set

"""


def only_diff_elements(set_1, set_2):
    """
    This functions returns a set of all different elements except in both sets

    Args:
        set_1: The first set
        set_2: The second set

    Return:
        A set of different elements except in set_1 and set_2
    """

    return (set_1 ^ set_2)
