#!/usr/bin/python3
"""

This module has one function that indents a text


"""


def text_indentation(text):
    """

    This function prints a text with two new lines after each
    (.), (?), or (:)

    Args:
        text (str): The text to be printed

    Raises:
        TypeError: If a non string object is passed

    """
    if not text:
        raise (0)

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    no_space = False

    for letter in text:
        if letter == '.':
            print('.\n\n', end='')
            no_space = True
        elif letter == '?':
            print('?\n\n', end='')
            no_space = True
        elif letter == ':':
            print(':\n\n', end='')
            no_space = True
        else:
            if no_space and letter == ' ':
                no_space = False
            else:
                print(letter, end='')
