#!/usr/bin/python3
"""

This module has one function returns a key with the biggest integer value

"""


def best_score(a_dictionary):
    """
    Find the biggest key's value and return its key

    Args:
        a_dictionary: Our target dic
    
    Return: 
        best_key: The biggest key's value
    """

    if not a_dictionary:
        return (None)

    best_value = 0
    best_key = ''

    for k, v in a_dictionary.items():
        if v > best_value:
            best_value = v
            best_key = k

    if best_key == '':
        return (None)

    return (best_key)
            
