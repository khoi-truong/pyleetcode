"""
Problem: Container With Most Water
"""

import unittest
from src.two_pointers.container_with_most_water import (
    ContainerWithMostWaterSolution,
    ContainerWithMostWaterTwoPointers,
)


class TestContainerWithMostWater(unittest.TestCase):
    """
    Test cases for container with most water problem
    """

    def test_max_area(self):
        sut = ContainerWithMostWaterTwoPointers()
        self._test_max_area(sut)

    def _test_max_area(self, sut: ContainerWithMostWaterSolution):
        self.assertEqual(sut.max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
        self.assertEqual(sut.max_area([1, 1]), 1)
        self.assertEqual(sut.max_area([4, 3, 2, 1, 4]), 16)
        self.assertEqual(sut.max_area([1, 2, 1]), 2)
        self.assertEqual(sut.max_area([2, 3, 4, 5, 18, 17, 6]), 17)
