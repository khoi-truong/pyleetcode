"""
Problem: Sort Colors
Leetcode: https://leetcode.com/problems/sort-colors
"""

from abc import ABC, abstractmethod


class Solution(ABC):
    @abstractmethod
    def sort_colors(self, nums: list[int]) -> None:
        pass


class TwoPointersSolution(Solution):
    """
    Solution: Two Pointers
    Time complexity: O(n)
    Space complexity: O(1)
    """

    def sort_colors(self, nums: list[int]) -> None:
        n = len(nums)
        red = 0
        white = 0
        blue = n - 1
        while red <= white <= blue:
            if nums[white] == 0:
                temp = nums[white]
                nums[white] = nums[red]
                nums[red] = temp
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                temp = nums[white]
                nums[white] = nums[blue]
                nums[blue] = temp
                blue -= 1
