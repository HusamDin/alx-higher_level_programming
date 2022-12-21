#!/usr/bin/python3

def safe_print_integer(value):
    """ Prints an integer with "{:d}".format().
    
    Args:
    value: Can be any type (integer, string, etc.)
    
    Returns:
    True if value has been correctly printed
    Otherwise, returns False
    """
    
    try:
        print("value = {:d}".format(value))
        return True
    except TypeError:
        return False
        
