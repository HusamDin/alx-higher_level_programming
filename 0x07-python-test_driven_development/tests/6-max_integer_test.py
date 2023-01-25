#!/usr/bin/python3
"""

This module is a unittest for the function max_integer([..])


"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    This class tests the max_integer function 
    """
    def test_max_integer_list(self):
        # Testing our function with a list of positive ints
        pos_list = [5, 1, 3, 8, 7]
        self.assertEqual(max_integer(pos_list), 8)

        # Testing our function with a list of negative ints
        neg_list = [-5, -8, -1, -3]
        self.assertEqual(max_integer(neg_list), -1)

    def test_max_integer_empty(self):
        # Testing our function with a list of 0 ints
        emp_list = []
        self.assertEqual(max_integer(emp_list), None)
