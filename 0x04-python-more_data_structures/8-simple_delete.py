#!/usr/bin/python3
"""

This module has one function to deletea key in a dic

"""


def simple_delete(a_dictionary, key=""):
    """
    Deletes a key in a dictionary

    Args:
        a_dictionary: A dictionary
        key: The key to be deleted

    Return:
        void
    """
    if key in a_dictionary:
        del a_dictionary[key]

    return a_dictionary
