"""
Problem: Valid Parentheses
Leetcode: https://leetcode.com/problems/valid-parentheses/
"""

from abc import ABC, abstractmethod


class ValidParenthesesSolution(ABC):
    """
    Abstract class for valid parentheses solutions
    """

    @abstractmethod
    def is_valid(self, s: str) -> bool:
        pass


class ValidParenthesesStack(ValidParenthesesSolution):
    """
    Solution: Stack
    """

    def is_valid(self, s: str) -> bool:
        if not s:
            return True
        pairs = {"(": ")", "[": "]", "{": "}"}
        stack = list[str]()
        for ch in s:
            if ch in {"(", "[", "{"}:
                stack.append(ch)
                continue
            if len(stack) == 0 or ch != pairs[stack[-1]]:
                return False
            stack.pop()
        return len(stack) == 0
