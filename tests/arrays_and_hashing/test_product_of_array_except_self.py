"""
Problem: Product of Array Except Self
"""
import unittest
from src.arrays_and_hashing.product_of_array_except_self import (
    ProductOfArrayExceptSelfPrefixAndSuffix,
    ProductOfArrayExceptSelfPrefixAndSuffixOptimised,
    ProductOfArrayExceptSelfSolution,
)


class TestProductOfArrayExceptSelf(unittest.TestCase):
    """
    Test cases for product of array except self problem
    """

    def test_product_of_array_except_self_prefix_and_suffix(self):
        sut = ProductOfArrayExceptSelfPrefixAndSuffix()
        self._test_product_of_array_except_self(sut)

    def test_product_of_array_except_self_prefix_and_suffix_optimised(self):
        sut = ProductOfArrayExceptSelfPrefixAndSuffixOptimised()
        self._test_product_of_array_except_self(sut)

    def _test_product_of_array_except_self(
        self,
        sut: ProductOfArrayExceptSelfSolution,
    ):
        self.assertListEqual(
            sut.product_except_self([1, 2, 3, 4]),
            [24, 12, 8, 6],
        )
        self.assertListEqual(
            sut.product_except_self([-1, 1, 0, -3, 3]),
            [0, 0, 9, 0, 0],
        )


if __name__ == "__main__":
    unittest.main()
