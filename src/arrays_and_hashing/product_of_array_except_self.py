"""
Problem: Product of Array Except Self
Leetcode: https://leetcode.com/problems/product-of-array-except-self/
"""

from abc import ABC, abstractmethod


class ProductOfArrayExceptSelfSolution(ABC):
    """
    Abstract class for product of array except self solutions
    """

    @abstractmethod
    def product_except_self(self, nums: list[int]) -> list[int]:
        pass


class ProductOfArrayExceptSelfPrefixAndSuffix(ProductOfArrayExceptSelfSolution):
    """
    Solution: Prefix and Suffix Products
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def product_except_self(self, nums: list[int]) -> list[int]:
        if not nums:
            return []
        prefix_product = [1] * len(nums)
        for i in range(len(nums)):
            num = nums[i]
            if i > 0:
                prefix_product[i] = prefix_product[i - 1] * num
            else:
                prefix_product[i] = num
        suffix_product = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            if i < len(nums) - 1:
                suffix_product[i] = suffix_product[i + 1] * num
            else:
                suffix_product[i] = num
        result = [1] * len(nums)
        for i in range(len(nums)):
            num = nums[i]
            if i > 0 and i < len(nums) - 1:
                result[i] = prefix_product[i - 1] * suffix_product[i + 1]
            elif i == 0:
                result[i] = suffix_product[i + 1]
            elif i == len(nums) - 1:
                result[i] = prefix_product[i - 1]
        return result


class ProductOfArrayExceptSelfPrefixAndSuffixOptimised(
    ProductOfArrayExceptSelfSolution
):
    """
    Solution: Prefix and Suffix Products
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def product_except_self(self, nums: list[int]) -> list[int]:
        if not nums:
            return []
        n = len(nums)
        result = [1] * n
        prefix = 1
        suffix = 1
        for i in range(n):
            result[i] *= prefix
            prefix *= nums[i]
            result[-1 - i] *= suffix
            suffix *= nums[-1 - i]
        return result
