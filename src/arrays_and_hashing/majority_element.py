"""
Problem: Majority Element
Leetcode: https://leetcode.com/problems/majority-element/
"""

from abc import ABC, abstractmethod
from collections import defaultdict


class MajorityElementSolution(ABC):
    @abstractmethod
    def majority_element(self, nums: list[int]) -> int:
        """
        Returns the majority element.
        """
        pass


class MajorityElementHashing(MajorityElementSolution):
    """
    Solution: Hashing
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def majority_element(self, nums: list[int]) -> int:
        frequency = defaultdict[int, int](int)
        n = len(nums)
        for num in nums:
            frequency[num] = frequency[num] + 1
            if frequency[num] > n // 2:
                return num
        return 0


class MajorityElementSorting(MajorityElementSolution):
    """
    Solution: Sorting
    Time Complexity: 0(n)
    Space Complexity: 0(1)
    """

    def majority_element(self, nums: list[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]
