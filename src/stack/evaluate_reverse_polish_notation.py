"""
Problem: Evaluate Reverse Polish Notation
Leetcode: https://leetcode.com/problems/evaluate-reverse-polish-notation/
"""

from abc import ABC, abstractmethod


class EvaluateReversePolishNotationSolution(ABC):
    @abstractmethod
    def eval_rpn(self, tokens: list[str]) -> int:
        pass


class EvaluateReversePolishNotationStack(EvaluateReversePolishNotationSolution):
    """
    Solution: Stack
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def eval_rpn(self, tokens: list[str]) -> int:
        stack = list[int]()
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                rhs, lhs = stack.pop(), stack.pop()
                value = self._calculate(lhs=lhs, rhs=rhs, operator=token)
                stack.append(value)
            else:
                stack.append(int(token))
        return stack[0]

    def _calculate(self, lhs: int, rhs: int, operator: str) -> int:
        if operator == "+":
            return lhs + rhs
        elif operator == "-":
            return lhs - rhs
        elif operator == "*":
            return lhs * rhs
        elif operator == "/":
            return int(lhs / rhs)
        return 0
