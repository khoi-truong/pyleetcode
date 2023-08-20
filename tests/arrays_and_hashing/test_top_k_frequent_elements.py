"""
Problem: Top K Frequent Elements
"""

import unittest
from src.arrays_and_hashing.top_k_frequent_elements import (
    TopKFrequentElementsDefaultdict,
    TopKFrequentElementsFixedArray,
    TopKFrequentElementsSolution,
)


class TestTopKFrequentElements(unittest.TestCase):
    """
    Test cases for top k frequent elements problem
    """

    def test_top_k_frequent_elements_defaultdict(self):
        sut = TopKFrequentElementsDefaultdict()
        self._test_top_k_frequent_elements(sut)

    def test_top_k_frequent_elements_fixed_array(self):
        sut = TopKFrequentElementsFixedArray()
        self._test_top_k_frequent_elements(sut)

    def _test_top_k_frequent_elements(self, sut: TopKFrequentElementsSolution):
        self.assertCountEqual(sut.top_k_frequent([1, 1, 1, 2, 2, 3], 2), [1, 2])
        self.assertCountEqual(sut.top_k_frequent([1], 1), [1])
        self.assertCountEqual(sut.top_k_frequent([1, 2], 2), [1, 2])
        self.assertCountEqual(sut.top_k_frequent([1, 2, 2], 1), [2])
        self.assertCountEqual(sut.top_k_frequent([1, 2, 2], 2), [1, 2])
        self.assertCountEqual(sut.top_k_frequent([1, 2, 2], 3), [1, 2])


if __name__ == "__main__":
    unittest.main()
