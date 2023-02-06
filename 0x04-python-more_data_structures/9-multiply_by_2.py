#!/usr/bin/python3
"""

This module has a function returns a new dic with all values multiplied by 2

"""


def multiply_by_2(a_dictionary):
    """
    Return a new dictionary with all values multiplied by 2

    Args:
        a_dictionary: Our target dic

    Return: new_dic
    """
    new_dic = a_dictionary.copy()

    for k, v in new_dic.items():
        new_dic[k] = v * 2

    return (new_dic)
