#!/usr/bin/python3
"""
This module has one function to replace all occurences of an element by another 

"""

def search_replace(my_list, search, replace):
    """
    This function replaces all occurences of an element by another in a new list
    
    Args: 
        my_list: the initial list
        search: the element to replace in the list
        replace: the new element in the list
    """

    new_list = my_list.copy()
    
    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace

    return (new_list)
 
