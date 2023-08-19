"""
Problem: Top K Frequent Elements
Leetcode: https://leetcode.com/problems/top-k-frequent-elements/
Solution: Hashing
Time Complexity: O(nlogk)
Space Complexity: O(n)
"""

from collections import defaultdict


class TopKFrequentElements:
    """
    Problem: Top K Frequent Elements
    """

    def top_k_frequent(self, nums: list[int], k: int) -> list[int]:
        """
        :param nums: list of integers
        :param k: number of top frequent elements
        :return: list of top k frequent elements
        """
        if not nums:
            return []
        frequencies = self._get_frequencies(nums)
        return self._get_top_k_frequent_elements(frequencies, k)

    def _get_frequencies(self, nums: list[int]) -> dict[int, int]:
        result = dict[int, int]()
        for num in nums:
            result[num] = result.get(num, 0) + 1
        return result

    def _get_top_k_frequent_elements(
        self,
        frequencies: dict[int, int],
        k: int,
    ) -> list[int]:
        reverse = defaultdict[int, list[int]](list)
        for key, value in frequencies.items():
            reverse[value].append(key)
        top_frequencies = sorted(reverse.keys(), reverse=True)
        result = list[int]()
        for frequency in top_frequencies:
            result += reverse[frequency]
        return result[0:k]
