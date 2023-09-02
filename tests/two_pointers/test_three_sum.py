"""
Problem: 3Sum
"""

import unittest
from src.two_pointers.three_sum import (
    ThreeSumTwoPointers,
    ThreeSumSolution,
)


class TestThreeSum(unittest.TestCase):
    """
    Test class for ThreeSumSolution
    """

    def test_three_sum_two_pointers(self):
        sut = ThreeSumTwoPointers()
        self._test_three_sum(sut)

    def _test_three_sum(self, sut: ThreeSumSolution):
        self.assertCountEqual(
            sut.three_sum([-1, 0, 1, 2, -1, -4]),
            [[-1, -1, 2], [-1, 0, 1]],
        )
        self.assertCountEqual(
            sut.three_sum([]),
            [],
        )
        self.assertCountEqual(
            sut.three_sum([0, 1, 1]),
            [],
        )
        self.assertCountEqual(
            sut.three_sum([0, 0, 0]),
            [[0, 0, 0]],
        )
        self.assertCountEqual(
            sut.three_sum([-2, 0, 0, 2, 2]),
            [[-2, 0, 2]],
        )
