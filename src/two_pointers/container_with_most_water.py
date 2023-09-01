"""
Problem: Container With Most Water
Leetcode: https://leetcode.com/problems/container-with-most-water/
"""

from abc import ABC, abstractmethod


class ContainerWithMostWaterSolution(ABC):
    @abstractmethod
    def max_area(self, height: list[int]) -> int:
        """
        Returns the max area of water that can be contained.
        """
        pass


class ContainerWithMostWaterTwoPointers(ContainerWithMostWaterSolution):
    """
    Solution: Two Pointers
    Reference: https://youtu.be/UuiTKBwPgAo
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def max_area(self, height: list[int]) -> int:
        n = len(height)
        if n < 2:
            return 0
        left = 0
        right = n - 1
        result = 0
        while left < right:
            result = max(result, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return result
