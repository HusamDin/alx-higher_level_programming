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

        # Testing our function with a list with max at the end
        end_max = [2, 1, 3, 5, 11]
        self.assertEqual(max_integer(end_max), 11)

        # Testing our function with a list with max at the beginning
        beg_max = [10, 6, 2, 5, 7, 9]
        self.assertEqual(max_integer(beg_max), 10)

        # Testing our function with a list with max at the beginning
        single_list = [1]
        self.assertEqual(max_integer(single_list), 1)

    def test_max_integer_empty(self):
        # Testing our function with a list of 0 ints
        emp_list = []
        self.assertEqual(max_integer(emp_list), None)
