#!/usr/bin/python3
"""

This module  has one function to print a dictionary by ordered keys

"""


def print_sorted_dictionary(a_dictionary):
    """
    Print a dictionary by ordered keys

    Args:
        a_dictionary: A dic to print its items by ordered keys

    Return:
        void
    """
    for key in sorted(a_dictionary):
        print(key + ':', end =' ')
        print(a_dictionary[key])
