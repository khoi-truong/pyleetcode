"""
Problem: Evaluate Reverse Polish Notation
"""

import unittest
from src.stack.evaluate_reverse_polish_notation import (
    EvaluateReversePolishNotationStack,
    EvaluateReversePolishNotationSolution,
)


class TestEvaluateReversePolishNotation(unittest.TestCase):
    """
    Test cases for evaluate reverse polish notation problem
    """

    def test_evaluate_reverse_polish_notation(self):
        sut = EvaluateReversePolishNotationStack()
        self._test_evaluate_reverse_polish_notation(sut)

    def _test_evaluate_reverse_polish_notation(
        self,
        sut: EvaluateReversePolishNotationSolution,
    ):
        self.assertEqual(sut.eval_rpn(["2", "1", "+", "3", "*"]), 9)
        self.assertEqual(sut.eval_rpn(["4", "13", "5", "/", "+"]), 6)
        self.assertEqual(
            sut.eval_rpn(
                ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
            ),
            22,
        )
