"""
Problem: Longest Consecutive Sequence
"""


import unittest

from src.arrays_and_hashing.longest_consecutive_sequence import (
    LongestConsecutiveSequenceSolution,
    LongestConsecutiveSequenceHashing,
)


class TestLongestConsecutiveSequence(unittest.TestCase):
    """
    Test cases for longest consecutive sequence problem
    """

    def test_longest_consecutive_sequence_hashing(self):
        sut = LongestConsecutiveSequenceHashing()
        self._test_longest_consecutive_sequence(sut)

    def _test_longest_consecutive_sequence(
        self, sut: LongestConsecutiveSequenceSolution
    ):
        self.assertEqual(sut.longest_consecutive([]), 0)
        self.assertEqual(sut.longest_consecutive([100, 4, 200, 1, 3, 2]), 4)
        self.assertEqual(sut.longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]), 9)
        self.assertEqual(sut.longest_consecutive([1, 2, 0, 1]), 3)
        self.assertEqual(sut.longest_consecutive([1, 2, 0, 1, 2]), 3)
