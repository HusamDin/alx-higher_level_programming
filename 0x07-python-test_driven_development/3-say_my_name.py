#!/usr/bin/python3
"""
    This module has one function <first name> <last name>

"""


def say_my_name(first_name, last_name=""):
    """
    This function prints My name is <first name> <last name>

    Args:
        first_name: A string
        last_name: A string

    Raises:
        TypeError: In case a non string is passed

    Returns:
        void
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print('My name is {} {}'.format(first_name, last_name))


