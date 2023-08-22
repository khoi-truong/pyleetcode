"""
Problem: Min Stack
Leetcode: https://leetcode.com/problems/min-stack/
"""


class MinStack:
    """
    Solution: Stack
    Time Complexity: O(1)
    """

    def __init__(self):
        self._min_stack = list[int]()
        self._stack = list[int]()

    def push(self, val: int) -> None:
        self._stack.append(val)
        if not self._min_stack:
            self._min_stack.append(val)
        else:
            self._min_stack.append(min(val, self.get_min()))

    def pop(self) -> None:
        self._stack.pop()
        self._min_stack.pop()

    def top(self) -> int:
        return self._stack[-1]

    def get_min(self) -> int:
        return self._min_stack[-1]
