"""
Problem: Reverse Words in a String
"""

import unittest
from src.two_pointers.reverse_words_in_a_string import (
    Solution,
    TwoPointersSolution,
)


class TestReverseWordsInAString(unittest.TestCase):
    """
    Test cases for Reverse Words in a String
    """

    def test_two_pointers_solution(self):
        sut = TwoPointersSolution()
        self._test_solution(sut)

    def _test_solution(self, sut: Solution):
        self.assertEqual(
            "blue is sky the",
            sut.reverse_words("the sky is blue"),
        )
        self.assertEqual(
            "world! hello",
            sut.reverse_words("  hello world!  "),
        )
        self.assertEqual(
            "example good a",
            sut.reverse_words("a good   example"),
        )
        self.assertEqual(
            "Alice Loves Bob",
            sut.reverse_words("  Bob    Loves  Alice   "),
        )
        self.assertEqual(
            "bob like even not does Alice",
            sut.reverse_words("Alice does not even like bob"),
        )
