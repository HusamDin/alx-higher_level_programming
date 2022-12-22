#!/usr/bin/python3

def safe_print_division(a, b):
    """ Divides 2 integers ande prints the result
    Args:
    a (int)
    b (int)

    Results: The value of the division
    """
    try:
        res = a / b
    except ZeroDivisionError:
        res = None
    finally:
        print("Inside result: {}".format(res))
    return res
