"""
Problem: Generate Parentheses
Leetcode: https://leetcode.com/problems/generate-parentheses/
"""

from abc import ABC, abstractmethod


class GenerateParenthesesSolution(ABC):
    """
    Abstract base class for Generate Parentheses solution
    """

    @abstractmethod
    def generate_parentheses(self, n: int) -> list[str]:
        pass


class GenerateParenthesesBacktracking(GenerateParenthesesSolution):
    """
    Solution: Backtracking
    Reference: https://youtu.be/s9fokUqJ76A
    """

    def generate_parentheses(self, n: int) -> list[str]:
        result = list[str]()

        def backtrack(partial: str, open_count: int, close_count: int):
            if open_count == close_count == n:
                result.append(partial)
                return
            if open_count < n:
                backtrack(
                    partial=partial + "(",
                    open_count=open_count + 1,
                    close_count=close_count,
                )
            if close_count < open_count:
                backtrack(
                    partial=partial + ")",
                    open_count=open_count,
                    close_count=close_count + 1,
                )

        backtrack("", 0, 0)
        return result


class GenerateParenthesesBacktrackingStack(GenerateParenthesesSolution):
    """
    Solution: Backtracking with Stack
    Reference: https://youtu.be/s9fokUqJ76A
    """

    def generate_parentheses(self, n: int) -> list[str]:
        result = list[str]()
        stack = list[str]()

        def backtrack(open_count: int, close_count: int):
            if open_count == close_count == n:
                completed = "".join(stack)
                result.append(completed)
                return
            if open_count < n:
                stack.append("(")
                backtrack(
                    open_count=open_count + 1,
                    close_count=close_count,
                )
                stack.pop()
            if close_count < open_count:
                stack.append(")")
                backtrack(
                    open_count=open_count,
                    close_count=close_count + 1,
                )
                stack.pop()

        backtrack(0, 0)
        return result
