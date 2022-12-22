#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """ Divide element by element 2 lists
    Args:
    my_list_1 (list)
    my_list_2 (list)
    list_length (int)

    Returns: new_list
    """
    new_list = []

    for i in range(list_length):
        try:
            res = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            res = 0
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        except IndexError:
            print("out of range")
            res = 0
        finally:
            new_list.append(res)
    return new_list
