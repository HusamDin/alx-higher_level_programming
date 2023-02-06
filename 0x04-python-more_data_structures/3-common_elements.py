#!/usr/bin/python3
"""

This module has one function to return a set of common elements

"""


def common_elements(set_1, set_2):
    """
    This functions returns a set of common elements in two sets

    Args:
        set_1: The first set
        set_2: The second set

    Return:
        A common set between set_1 and set_2
    """

    return (set_1 & set_2)
