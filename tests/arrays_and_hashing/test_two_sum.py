"""
Problem: Two Sum
"""

import unittest
from src.arrays_and_hashing.two_sum import two_sum


class TestTwoSum(unittest.TestCase):
    """
    Test cases for two sum problem
    """

    def test_two_sum(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(two_sum([3, 2, 4], 6), [1, 2])
        self.assertEqual(two_sum([3, 3], 6), [0, 1])

    def test_two_sum_with_empty_array(self):
        self.assertEqual(two_sum([], 6), [])

    def test_two_sum_with_one_element(self):
        self.assertEqual(two_sum([1], 6), [])
