"""
Problem: Minimum Window Substring
"""

import unittest
from src.sliding_window.minimum_window_substring import (
    Solution,
    SlidingWindowSolution,
)


class TestMinimumWindowSubstring(unittest.TestCase):
    """
    Test Minimum Window Substring
    """

    def test_sliding_window_solution(self):
        sut = SlidingWindowSolution()
        self._test_solution(sut)

    def _test_solution(self, sut: Solution):
        self.assertEqual(
            sut.min_window("ADOBECODEBANC", "ABC"),
            "BANC",
        )
        self.assertEqual(
            sut.min_window("a", "a"),
            "a",
        )
        self.assertEqual(
            sut.min_window("a", "aa"),
            "",
        )


if __name__ == "__main__":
    unittest.main()
