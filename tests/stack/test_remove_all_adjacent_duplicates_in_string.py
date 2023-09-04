"""
Problem: Remove All Adjacent Duplicates in String
"""

import unittest
from src.stack.remove_all_adjacent_duplicates_in_string import (
    Solution,
    StackSolution,
)


class TestRemoveAllAdjacentDuplicatesInString(unittest.TestCase):
    def test_stack_solution(self):
        sut = StackSolution()
        self._test(sut)

    def _test(self, sut: Solution):
        self.assertEqual(sut.remove_duplicates("abbaca"), "ca")
        self.assertEqual(sut.remove_duplicates("azxxzy"), "ay")
