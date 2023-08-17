"""
Problem: Two Sum
Leetcode: https://leetcode.com/problems/two-sum/
Solution: Hashing
Time Complexity: O(n)
Space Complexity: O(n)
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    """
    :param nums: list of integers
    :param target: target sum
    :return: indices of the two numbers such that they add up to target
    """
    if not nums:
        return []
    seen = dict[int, int]()
    for index, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], index]
        seen[num] = index
    return []
