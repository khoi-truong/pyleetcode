"""
Problem: Generate Parentheses
"""

import unittest
from src.stack.generate_parentheses import (
    GenerateParenthesesSolution,
    GenerateParenthesesBacktracking,
    GenerateParenthesesBacktrackingStack,
)


class TestGenerateParentheses(unittest.TestCase):
    """
    Test class for Generate Parentheses
    """

    def test_generate_parenteses_backtracking(self):
        sut = GenerateParenthesesBacktracking()
        self._test_generate_parenteses(sut)

    def test_generate_parenteses_backtracking_stack(self):
        sut = GenerateParenthesesBacktrackingStack()
        self._test_generate_parenteses(sut)

    def _test_generate_parenteses(self, sut: GenerateParenthesesSolution):
        self.assertEqual(
            ["()"],
            sut.generate_parentheses(n=1),
        )
        self.assertEqual(
            ["(())", "()()"],
            sut.generate_parentheses(n=2),
        )
        self.assertEqual(
            ["((()))", "(()())", "(())()", "()(())", "()()()"],
            sut.generate_parentheses(n=3),
        )
