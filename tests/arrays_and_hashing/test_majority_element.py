"""
Problem: Majority Element
"""

import unittest
from src.arrays_and_hashing.majority_element import (
    MajorityElementHashing,
    MajorityElementSorting,
    MajorityElementSolution,
)


class TestMajorityElement(unittest.TestCase):
    """
    Test cases for majority element problem
    """

    def test_majority_element_hashing(self):
        sut = MajorityElementHashing()
        self._test_majority_element(sut)

    def test_majority_element_sorting(self):
        sut = MajorityElementSorting()
        self._test_majority_element(sut)

    def _test_majority_element(self, sut: MajorityElementSolution):
        self.assertEqual(sut.majority_element([3, 2, 3]), 3)
        self.assertEqual(sut.majority_element([2, 2, 1, 1, 1, 2, 2]), 2)
