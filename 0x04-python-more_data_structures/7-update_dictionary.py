#!/usr/bin/python3
"""

This module has one function replaces or adds key/value in a dictionary.

"""


def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds key/value pairs

    Args:
        a_dictionary: A dic
        key: Always a key string
        value: Can be any type

    Return:
        new_dic: An updated dic
    """

    for k, v in a_dictionary.items():
        if k not in a_dictionary:
            a_dictionary[key] = value

    a_dictionary[key] = value
    return (a_dictionary)
