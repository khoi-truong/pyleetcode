"""
Problem: Sort Colors
"""

import unittest
from src.two_pointers.sort_colors import (
    Solution,
    TwoPointersSolution,
)


class TestSortColors(unittest.TestCase):
    """
    Test case for Sort Colors
    """

    def test_two_pointers_solution(self):
        sut = TwoPointersSolution()
        self._test_solution(sut)

    def _test_solution(self, sut: Solution):
        nums = [2, 0, 2, 1, 1, 0]
        sut.sort_colors(nums)
        self.assertEqual(nums, [0, 0, 1, 1, 2, 2])

        nums = [2, 0, 1]
        sut.sort_colors(nums)
        self.assertEqual(nums, [0, 1, 2])

        nums = [0]
        sut.sort_colors(nums)
        self.assertEqual(nums, [0])

        nums = [1]
        sut.sort_colors(nums)
        self.assertEqual(nums, [1])
