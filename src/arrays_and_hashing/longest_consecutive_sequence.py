"""
Problem: Longest Consecutive Sequence
Leetcode: https://leetcode.com/problems/longest-consecutive-sequence/
"""

from abc import ABC, abstractmethod

# TODO: Add union-find solution


class LongestConsecutiveSequenceSolution(ABC):
    """
    Abstract class for Longest Consecutive Sequence
    """

    @abstractmethod
    def longest_consecutive(self, nums: list[int]) -> int:
        pass


class LongestConsecutiveSequenceHashing(LongestConsecutiveSequenceSolution):
    """
    Solution: Hashing
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def longest_consecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        seen = set[int](nums)
        result = 0
        for num in nums:
            if num - 1 not in seen:
                length = 1
                while num + length in seen:
                    length += 1
                result = max(result, length)
        return result
