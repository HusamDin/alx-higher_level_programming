#!/usr/bin/python3
"""
This module has one function to return the number of keys

"""


def number_keys(a_dictionary):
    """
    Return the number of keys in a dictionary

    Args:
        a_dictionary: A dictionary with 0 or more keys

    Returns:
        no_keys: The number of keys
    """
    no_keys = 0

    for k in a_dictionary.items():
        no_keys += 1

    return (no_keys)
