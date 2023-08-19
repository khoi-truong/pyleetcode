"""
Problem: Top K Frequent Elements
"""

import unittest
from src.arrays_and_hashing.top_k_frequent_elements import TopKFrequentElements


class TestTopKFrequentElements(unittest.TestCase):
    """
    Test cases for top k frequent elements problem
    """

    def test_top_k_frequent_elements_defaultdict(self):
        sut = TopKFrequentElements()
        solutions = [
            sut.top_k_frequent_defaultdict,
            sut.top_k_frequent_fixed_array,
        ]
        for solution in solutions:
            self.assertCountEqual(solution([1, 1, 1, 2, 2, 3], 2), [1, 2])
            self.assertCountEqual(solution([1], 1), [1])
            self.assertCountEqual(solution([1, 2], 2), [1, 2])
            self.assertCountEqual(solution([1, 2, 2], 1), [2])
            self.assertCountEqual(solution([1, 2, 2], 2), [1, 2])
            self.assertCountEqual(solution([1, 2, 2], 3), [1, 2])


if __name__ == "__main__":
    unittest.main()
