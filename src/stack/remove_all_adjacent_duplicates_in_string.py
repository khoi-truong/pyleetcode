"""
Problem: Remove All Adjacent Duplicates in String
Leetcode: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string
"""

from abc import ABC, abstractmethod


class Solution(ABC):
    @abstractmethod
    def remove_duplicates(self, s: str) -> str:
        pass


class StackSolution(Solution):
    def remove_duplicates(self, s: str) -> str:
        stack = list[str]()
        for ch in s:
            if stack and ch == stack[-1]:
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)
