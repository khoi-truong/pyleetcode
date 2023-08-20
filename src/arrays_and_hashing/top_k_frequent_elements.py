"""
Problem: Top K Frequent Elements
Leetcode: https://leetcode.com/problems/top-k-frequent-elements/
Solution: Hashing
Time Complexity: O(nlogk)
Space Complexity: O(n)
"""

from collections import defaultdict
from abc import ABC, abstractmethod

# TODO: Add heap solution
# TODO: Add quick select solution
# TODO: Add bucket sort solution


class TopKFrequentElementsSolution(ABC):
    """
    Abstract class for top k frequent elements solutions
    """

    @abstractmethod
    def top_k_frequent(self, nums: list[int], k: int) -> list[int]:
        """
        :param nums: list of integers
        :param k: number of top frequent elements
        :return: list of top k frequent elements
        """
        pass

    def _get_frequencies(self, nums: list[int]) -> dict[int, int]:
        result = dict[int, int]()
        for num in nums:
            result[num] = result.get(num, 0) + 1
        return result


class TopKFrequentElementsDefaultdict(TopKFrequentElementsSolution):
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
        return self._get_top_k_frequent_elements_defaultdict(
            frequencies=self._get_frequencies(nums),
            k=k,
        )

    def _get_top_k_frequent_elements_defaultdict(
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


class TopKFrequentElementsFixedArray(TopKFrequentElementsSolution):
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
        return self._get_top_k_frequent_elements_fixed_array(
            count=len(nums),
            frequencies=self._get_frequencies(nums),
            k=k,
        )

    def _get_top_k_frequent_elements_fixed_array(
        self,
        count: int,
        frequencies: dict[int, int],
        k: int,
    ) -> list[int]:
        nums_with_frequency = [list[int]() for _ in range(count + 1)]
        for num, frequency in frequencies.items():
            nums_with_frequency[frequency].append(num)
        result = list[int]()
        for frequency in range(len(nums_with_frequency) - 1, 0, -1):
            for nums in nums_with_frequency[frequency]:
                result.append(nums)
                if len(result) == k:
                    return result
        return result
