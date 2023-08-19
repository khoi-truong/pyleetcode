"""
Problem: Top K Frequent Elements
"""

import unittest
from src.arrays_and_hashing.top_k_frequent_elements import TopKFrequentElements


class TestTopKFrequentElements(unittest.TestCase):
    """
    Test cases for top k frequent elements problem
    """

    def test_top_k_frequent_elements(self):
        sut = TopKFrequentElements()
        self.assertCountEqual(
            sut.top_k_frequent([1, 1, 1, 2, 2, 3], 2),
            [1, 2],
        )
        self.assertCountEqual(
            sut.top_k_frequent([1], 1),
            [1],
        )
        self.assertCountEqual(
            sut.top_k_frequent([1, 2], 2),
            [1, 2],
        )
