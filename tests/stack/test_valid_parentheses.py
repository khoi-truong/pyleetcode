"""
Problem: Valid Parentheses
"""

import unittest
from src.stack.valid_parentheses import (
    ValidParenthesesSolution,
    ValidParenthesesStack,
)


class TestValidParenthesesStack(unittest.TestCase):
    """
    Test cases for valid parentheses problem
    """

    def test_valid_parentheses(self):
        sut = ValidParenthesesStack()
        self._test_valid_parentheses(sut)

    def _test_valid_parentheses(self, sut: ValidParenthesesSolution):
        self.assertTrue(sut.is_valid("()"))
        self.assertTrue(sut.is_valid("()[]{}"))
        self.assertFalse(sut.is_valid("(]"))
        self.assertFalse(sut.is_valid("([)]"))
        self.assertTrue(sut.is_valid("{[]}"))
        self.assertFalse(sut.is_valid("]"))
        self.assertFalse(sut.is_valid("(("))
        self.assertFalse(sut.is_valid("){"))
        self.assertFalse(sut.is_valid("){"))
        self.assertFalse(sut.is_valid("(("))
        self.assertFalse(sut.is_valid("(("))
        self.assertFalse(sut.is_valid("(])"))
