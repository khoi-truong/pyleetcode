"""
Problem: 3Sum
Leetcode: https://leetcode.com/problems/3sum/
"""

from abc import ABC, abstractmethod


class ThreeSumSolution(ABC):
    @abstractmethod
    def three_sum(self, nums: list[int]) -> list[list[int]]:
        pass


class ThreeSumTwoPointers(ThreeSumSolution):
    """
    Solution: Two Pointers
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """

    def three_sum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        result = list[list[int]]()
        for index, num in enumerate(nums):
            if num > 0:
                return result
            if index > 0 and num == nums[index - 1]:
                continue
            left, right = index + 1, n - 1
            while left < right:
                two_sum = nums[left] + nums[right]
                if two_sum > -num:
                    right -= 1
                elif two_sum < -num:
                    left += 1
                else:
                    result.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return result
